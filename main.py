def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def api_table(name, path, method='get', parameters=[]):

        param = ', '.join(f'`{p}`' for p in parameters)

        return f"| Name | Route | Method | Query Parameters | \n\
        | :-----| :-----| :----- | :----- | \n\
        | {name} | `/api/v0/{path}` | `{method}` | {param} | \n\n"


    @env.macro
    def usage_api_macro(path, method='get', parameters={}):

        if len(parameters) > 0:
            param = "?" + '&'.join(f'{k}={v}' for k, v in parameters.items())
        else:
            param = ""

        return f"`{method}` - `http://localhost:5340/api/v0/{path}{param}`"

