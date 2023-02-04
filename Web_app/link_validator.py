def link_validation(url):
    validarots = ['steam://rungame/730/','+csgo_econ_action_preview%20','M','A','D']
    if url.__contains__(validarots[0]) and url.__contains__(validarots[1]) and url.__contains__(validarots[2]) and url.__contains__(validarots[3]) and url.__contains__(validarots[4]):
        return True
    else:
        return False