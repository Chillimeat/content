import demistomock as demisto


def get_feed_config(sub_feeds):
    feed_name_to_config = {
        'AMAZON': {
            'url': 'https://ip-ranges.amazonaws.com/ip-ranges.json',
            'extractor': "prefixes[?service=='AMAZON']",
            'indicator': 'ip_prefix',
            'indicator_type': FeedIndicatorType.IP,
            'fields': ['region', 'service']
        },
        'EC2': {
            'url': 'https://ip-ranges.amazonaws.com/ip-ranges.json',
            'extractor': "prefixes[?service=='EC2']",
            'indicator': 'ip_prefix',
            'indicator_type': FeedIndicatorType.IP,
            'fields': ['region', 'service']
        },
        'ROUTE53': {
            'url': 'https://ip-ranges.amazonaws.com/ip-ranges.json',
            'extractor': "prefixes[?service=='ROUTE53']",
            'indicator': 'ip_prefix',
            'indicator_type': FeedIndicatorType.IP,
            'fields': ['region', 'service']
        },
        'ROUTE53_HEALTHCHECKS': {
            'url': 'https://ip-ranges.amazonaws.com/ip-ranges.json',
            'extractor': "prefixes[?service=='ROUTE53_HEALTHCHECKS']",
            'indicator': 'ip_prefix',
            'indicator_type': FeedIndicatorType.IP,
            'fields': ['region', 'service']
        },
        'CLOUDFRONT': {
            'url': 'https://ip-ranges.amazonaws.com/ip-ranges.json',
            'extractor': "prefixes[?service=='CLOUDFRONT']",
            'indicator': 'ip_prefix',
            'indicator_type': FeedIndicatorType.IP,
            'fields': ['region', 'service']
        },
        'S3': {
            'url': 'https://ip-ranges.amazonaws.com/ip-ranges.json',
            'extractor': "prefixes[?service=='S3']",
            'indicator': 'ip_prefix',
            'indicator_type': FeedIndicatorType.IP,
            'fields': ['region', 'service']
        }
    }

    return [feed for feed in feed_name_to_config if feed in sub_feeds]



from JSONFeedApiModule import *  # noqa: E402


def main():
    params = demisto.params()
    params['feed_name_to_config'] = get_feed_config(params.get('sub_feeds', ['AMAZON']))
    feed_main(params, 'AWS Feed')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()