import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv

from libs.client import EStatClient

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)


def get_client(app_id: str) -> EStatClient:
    return EStatClient(app_id=app_id)


def main():
    app_id = os.getenv("E_STAT")
    esc = get_client(app_id)
    r = esc.get("0003343671")
    meta_info = r.json()
    # meta_info_keys = meta_info["GET_META_INFO"].keys()
    # print(meta_info_keys)
    # result = meta_info["GET_META_INFO"]["RESULT"]
    # print(result)
    # param = meta_info["GET_META_INFO"]["PARAMETER"]
    # print(param)
    # info = meta_info["GET_META_INFO"]["METADATA_INF"].keys()
    # print(info)
    # print(len(meta_info["GET_META_INFO"]["METADATA_INF"]["CLASS_INF"]["CLASS_OBJ"]))
    class_obj = meta_info["GET_META_INFO"]["METADATA_INF"]["CLASS_INF"]["CLASS_OBJ"][1][
        "CLASS"
    ]
    result = [item for item in class_obj if "電気代" in item["@name"]]
    print(result)
    # [{'@code': '030100000', '@name': '3.1 電気代', '@level': '2', '@unit': '円', '@parentCode': '030000000'}]


if __name__ == "__main__":
    main()
