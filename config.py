# 验证码解析参数
verify_code_params = {
    'user': 'mijiu2024',
    'pass': 'xswl123456789',
    'softid': '964167',
    'codetype': 1902,
    'file_base64': ''
}

# 验证码解析请求头
verify_code_headers = {
    'Connection': 'Keep-Alive',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
}

# 讲座系统请求头
lecture_headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Host': 'ehall.seu.edu.cn',
    'Origin': 'http://ehall.seu.edu.cn',
    'Referer': 'http://ehall.seu.edu.cn/gsapp/sys/yddjzxxtjappseu/*default/index.do',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'X-Requested-With': 'XMLHttpRequest',
    # 每次操作前修改cookie
    'Cookie': "route=de1353bd2eecd92e44c51ddb2c26661d; route=a582dc4be54fe74b7d8abd1ec14e5b0b; EMAP_LANG=zh; THEME=indigo; GS_SESSIONID=d90b0341b8d3ba3c9a8658fd0e4489c9; _WEU=WwnVMD*QRwBFn11UaddaHpFoWQgpyNAzkAV0nQwhR1Unm8YJTqb3E7F1OtPI_av16k8zNBJZ5NalzHTA6iem8Sgvszrv3KFOpRZNdRbWWEWuyMaR*AYUAK1a0C7tggHcyYYyy4J8Hy9If23NbhppClZRfMrhgFmz7O1P6yXGYhYSpkLH8DKqK_SBIqvgrEaK6EC44DNHRPQkf8Fg9gWdB09ohS_F9RaKRSKDIAM1X7uPDRqZheOpoMvShnEhcNFG9GoYxTU1efLaElLV7r49xJbG7RtEoP27nDYG952LfAu2CtlB4wQF9yVKT3LyQH26XiNHHgej58PaiTKUB1m6dA*Jb63y2lu6; amp.locale=zh_CN; JSESSIONID=Sju0CDkhHi4agNsG05yi90A1B-Kv1ciR-FE9N2zHIFAe5c9sArWI!49887105"
}

# 目标讲座关键词，请尽可能指向唯一目标
lecture_key = "自信中国"