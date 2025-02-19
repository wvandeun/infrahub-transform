from infrahub_sdk.transforms import InfrahubTransform


class DeviceConfigTransform(InfrahubTransform):

    query = "device_config_query"

    async def transform(self, data):
        device = data["NetworkDevice"]["edges"][0]["node"]
        device_name = device["name"]["value"]
        device_description = device["description"]["value"]

        return {
            "device_hostname": device_name,
            "device_description": f"*{device_description}*",
            "new_key": "new_valye"
        }
