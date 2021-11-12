#!python

"""
CLI to landscape API
"""

if __name__ == '__main__':

    import argh
    import atooms.energy_landscape.api
    argh.dispatch_commands(atooms.energy_landscape.api.pes)
    
