import pyrfc
# print(pyrfc.__version__)
# print(pyrfc.get_nwrfclib_version())
conn_params = {
    "user": "Z_RFC",
    "passwd": "123456",
    "ashost": "192.168.7.63",
    "sysnr": "00",
    "lang": "ZH",
    "client": "310"
}

conn = pyrfc.Connection(**conn_params)

result = conn.call("ZLK001_F02",I_DATA1="20221101",I_DATA2="20221130")

print(result["ET_DATA"])