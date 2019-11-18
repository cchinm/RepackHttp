#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''

 * @version: 0.0.0
 * @Company: 
 * @Author: zhanming.zhang 
 * @Date: 2019/11/16 15:53 
 * @Last Modified by:   zhanming.zhang 
 * @Last Modified time: 2019/11/16 15:53
 * @Desc: 
'''

from RepackHttp.Http import (requests,
                  logging,
                  traceback)
from RepackHttp.Http.response import Response


class FetchRequest:



    def fetch(self, request):
        logging.debug("sadf")
        logging.debug("%s %s" % (request, request.url))
        try:
            proxies = request.meta.get('proxy', None)
            _resp = requests.request(
                method=request.method,
                url=request.url,
                headers=request.headers,
                proxies=proxies
            )
            resp = Response(url=_resp.url,
                            request=request,
                            response=_resp,
                            headers=_resp.headers,
                            **request.meta)
            if request.callback:
                return request.callback(resp)
            return resp
        except:
            traceback.print_stack()
            logging.error("Fetch Error %s %s" % (request, request.url))
            logging.debug("Error Reason: "+traceback.format_exc() )


