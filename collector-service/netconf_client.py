from ncclient import manager


def netconf_connect(olt):
    try:
        return manager.connect(
            host=olt['ip'],
            port=830,
            username=olt['username'],
            password=olt['password'],
            hostkey_verify=False,
            timeout=10
        )
    except Exception as e:
        print(f"NETCONF error: {e}")
        return None