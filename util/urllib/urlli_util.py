# coding: utf-8
import urllib.request
import ssl


def http_request(url, headers, body, proxy=None, cafile=None, certfile=None, keyfile=None, password=None):
    if proxy is not None:
        proxy_client(aws_config.PROXY_PROTOCOL, PROXY_URL)
    if cafile is not None:
        sslctx = ssl_client(cafile=cafile, certfile=certfile,
                            keyfile=keyfile, password=password)
    req = urllib.request.Request(url, body.encode(), headers)
    with urllib.request.urlopen(req, context=sslctx) as res:
        body = res.read()
    return body


def http_connection(url, header={}):
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    return response


def http_get(url, header={}):
    request = urllib.request.Request(url=url, headers=header)
    with urllib.request.urlopen(request) as response:
        body = response.read()
    return response


def proxy_client(protocol, url):
    proxy = urllib.request.ProxyHandler({protocol: url})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)


def ssl_client(cafile=None, certfile=None, keyfile=None, password=None):
    sslctx = ssl.create_default_context()
    sslctx.load_verify_locations(
        cafile=cafile)
    sslctx.load_cert_chain(
        certfile=certfile, keyfile=keyfile, password=password)
    return sslctx
