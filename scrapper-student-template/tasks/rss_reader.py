from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import html
from datetime import datetime
import json as js
import xml.etree.ElementTree as ET

class UnhandledException(Exception):
    pass


def rss_parser(
    xml_str: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Parses an RSS XML string, extracts channel and items information.

    Args:
        xml_str: XML document as a string.
        limit: Maximum number of items to include. If None, include all items.
        json: If True, return a JSON representation as a single-element list.

    Returns:
        List of strings (plain output) or a single-element list with a JSON string.
    """
    try:
        root = ET.fromstring(xml_str)
    except ET.ParseError:
        return []

    channel = root.find('channel')
    if channel is None:
        return []

    result: List[str] = []
    result_json: dict = {}

    # Required channel fields
    title = channel.findtext('title')
    link = channel.findtext('link')
    description = channel.findtext('description')
    if title:
        t = html.unescape(title)
        result.append(f"Feed: {t}")
        result_json['title'] = t
    if link:
        l = html.unescape(link)
        result.append(f"Link: {l}")
        result_json['link'] = l

    # Optional channel fields
    last_build = channel.findtext('lastBuildDate')
    if last_build:
        lb = html.unescape(last_build)
        result.append(f"Last Build Date: {lb}")
        result_json['lastBuildDate'] = lb

    pub_date = channel.findtext('pubDate')
    if pub_date:
        pd = html.unescape(pub_date)
        result.append(f"Publish Date: {pd}")
        result_json['pubDate'] = pd

    language = channel.findtext('language')
    if language:
        lang = html.unescape(language)
        result.append(f"Language: {lang}")
        result_json['language'] = lang

    # Categories
    chan_cats = [html.unescape(c.text) for c in channel.findall('category') if c.text]
    if chan_cats:
        result.append(f"Categories: {', '.join(chan_cats)}")
        result_json['category'] = chan_cats

    # Editor
    editor = channel.findtext('managingEditor') or channel.findtext('managinEditor')
    if editor:
        ed = html.unescape(editor)
        result.append(f"Editor: {ed}")
        result_json['managingEditor'] = ed

    # Other optional channel fields
    for tag in ['docs', 'generator', 'copyright', 'rating', 'skipDays', 'skipHours', 'textInput', 'ttl', 'webMaster']:
        val = channel.findtext(tag)
        if val:
            v = html.unescape(val)
            label = tag[0].upper() + tag[1:]
            result.append(f"{label}: {v}")
            result_json[tag] = v

    # Only include description in JSON
    if description:
        d = html.unescape(description)
        result_json['description'] = d
    # Plain channel description
    if description:
        d_plain = html.unescape(description)
        result.append(f"Description: {d_plain}")

    # Items
    items_json: List[dict] = []
    items = channel.findall('item')
    for idx, item in enumerate(items):
        if limit is not None and idx >= limit:
            break
        entry: dict = {}
        # item elements
        # title
        it = item.findtext('title')
        if it:
            val = html.unescape(it)
            result.append(f"Title: {val}")
            entry['title'] = val
        # pubDate
        ip = item.findtext('pubDate')
        if ip:
            val = html.unescape(ip)
            result.append(f"Publish Date: {val}")
            entry['pubDate'] = val
        # link
        il = item.findtext('link')
        if il:
            val = html.unescape(il)
            result.append(f"Link: {val}")
            entry['link'] = val
        # description
        idesc = item.findtext('description')
        if idesc:
            val = html.unescape(idesc)
            result.append(f"\n{val}")
            entry['description'] = val
        # author
        auth = item.findtext('author')
        if auth:
            val = html.unescape(auth)
            result.append(f"Author: {val}")
            entry['author'] = val
        # category
        itcats = [html.unescape(c.text) for c in item.findall('category') if c.text]
        if itcats:
            # for single item, singular label
            result.append(f"Category: {', '.join(itcats)}")
            entry['category'] = itcats
        # comments
        com = item.findtext('comments')
        if com:
            val = html.unescape(com)
            result.append(f"Comments: {val}")
            entry['comments'] = val
        # guid
        guid = item.findtext('guid')
        if guid:
            val = html.unescape(guid)
            result.append(f"Guid: {val}")
            entry['guid'] = val
        # source
        src = item.find('source')
        if src is not None:
            text = src.text or ''
            val = html.unescape(text)
            result.append(f"Source: {val}")
            entry['source'] = val
        items_json.append(entry)

    # include items in JSON only if present
    if items_json:
        result_json['items'] = items_json

    if json:
        return [js.dumps(result_json, indent=2)]
    return result


def main(argv: Optional[Sequence] = None):
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL or file", type=str, nargs="?"
    )
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )
    headers = {"User-Agent": "Mozilla/5.0"}
    args = parser.parse_args(argv)
    try:
        if args.source and args.source.startswith(('http://', 'https://')):
            xml_content = requests.get(args.source, headers=headers).text
        else:
            with open(args.source, 'r', encoding='utf-8') as f:
                xml_content = f.read()
        print("\n".join(rss_parser(xml_content, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)

if __name__ == "__main__":
    main()
