import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f1c6f2cb'.decode('hex')
P2P_PORT = 1986
ADDRESS_VERSION = 23
RPC_PORT = 1987
RPC_CHECK =RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'australiacash' in (yield bitcoind.rpc_help()) 
            (yield helper.check_block_header(bitcoind, 'aa43989047f144331fc6400859c691b11c0e111ead1977511d340860c1c5ad1f')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'AUS'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Australiacash') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Australiacash/') if platform.system() == 'Darwin' else os.path.expanduser('~/.australiacash'), 'australiacash.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://'
ADDRESS_EXPLORER_URL_PREFIX = 'https://'
TX_EXPLORER_URL_PREFIX = 'https://'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
