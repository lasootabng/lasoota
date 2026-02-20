# from json import load as j_load
# from os.path import dirname, abspath



# def get_config(source="datasource", key=None) -> dict | str | None:
#     """ Get config json """

#     root_dir = dirname(dirname(abspath(__file__)))

#     try:
#         with open(root_dir + "/configuration/config.json", "r") as fp:
#             return j_load(fp)[source][key]
#     except FileNotFoundError:
#         return ''
    
# def get_price_list():
#     root_dir = dirname(dirname(abspath(__file__)))
#     with open(root_dir + "/configuration/price_list.json", "r") as fp:
#         return j_load(fp)



# def response_formatter(data, error=False, status_code=200, status_value="OK"):
#     """ Response handler """
#     # Version change - Major.Minor.Patch
#     return {"version": {"name": "freelancer-engine", "version": "0.0.1"},
#             "status": {"code": status_code, "value": status_value},
#             "data": data, "error": error}
