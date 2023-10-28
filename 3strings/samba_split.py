# ***********************
# SEPARANDO RECURSO SAMBA
# ***********************


def run(smb_path: str) -> tuple:
    # TU CÓDIGO AQUÍ
    smb_path = smb_path.lstrip("/")
    index_barra = smb_path.find("/")
    host, path = smb_path[:index_barra], smb_path[index_barra:]
    return host, path


if __name__ == '__main__':
    run('//1.1.1.1/aprende/python')