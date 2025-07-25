from world_abstract import *

weth = load_contract('weth', WETH_PLUME)
oethp = load_contract('ousd', OETHP)
woeth = load_contract('ERC20', BRIDGED_WOETH_PLUME)
woeth_plume = load_contract('wrapped_ousd', WOETH_PLUME)

plume_strategist = brownie.accounts.at(MULTICHAIN_STRATEGIST, force=True)
from_strategist = {'from':MULTICHAIN_STRATEGIST}

vault_admin = load_contract('vault_admin', OETHP_VAULT_PROXY)
vault_core = load_contract('vault_core', OETHP_VAULT_PROXY)
vault_value_checker = load_contract('vault_value_checker', OETHP_VAULT_VALUE_CHECKER)

woeth_strat = load_contract('woeth_strategy', OETHP_WOETH_STRATEGY)

oethpWETHpool = load_contract('maverick_v2_pool', "0x3F86B564A9B530207876d2752948268b9Bf04F71")
plume_woeth_omnichain_adapter = load_contract('omnichain_l2_adapter', PLUME_WOETH_OMNICHAIN_ADAPTER)
plume_bridge_helper_module = load_contract('plume_bridge_helper', PLUME_BRIDGE_HELPER_MODULE)
