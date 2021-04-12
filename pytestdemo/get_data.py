import yaml


def get_calculatorTestData(operational: str) -> list:
    with open(f"datas/{operational}.yaml", encoding='utf-8') as f:
        test_datas = yaml.safe_load(f)
    get_datas = test_datas["datas"]
    get_ids = test_datas["ids"]
    return [get_datas, get_ids]