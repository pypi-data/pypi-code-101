from distutils.core import setup
setup(
  name = 'discord_wallet',
  packages = ['discord_wallet'],
  version = '0.1',
  description = 'Connect your bot to Discord Wallet.',
  author = 'Panicakr',
  url = 'https://github.com/user/panicakr',
  download_url = 'https://github.com/panicakr/discord_wallet/archive/v_01.tar.gz',
  keywords = ['discord', 'discord.py', 'economy'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
  ],
)