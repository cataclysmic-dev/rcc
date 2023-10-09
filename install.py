"""
Handles all the packages
"""
import os, sys, getch
import log

def qts():
    if input("\033[1;33mreccomendation \033[0m\033[90mCORE rcc:\033[0m would you like to install qts alongside rbxts? (y/n)  ") == "y":
        install("qts")
    else:
        return True
    
def installrbxts():
    print("\033[1;33minfo \033[0m\033[90mCORE rcc:\033[0m rbxts requires npm to be installed")
    os.system("npm install -g typescript")
    os.system("npm install -g @rbxts/rbxts-cli")
    
def notact():
    log.error("not available")
    
exec = {
    "roblox-py": {
        "repo": "roblox-compilers/roblox-py",
        "darwin": "rbxpy",
        "win32": "rbxpy.exe",
        "special": None
    }, 
    "roblox-c": {
        "repo": "roblox-compilers/roblox-c",
        "darwin": "rbxc",
        "win32": "rbxc.exe",
        "special": notact
    }, 
    "roblox-cs": {
        "repo": "roblox-compilers/roblox-cs",
        "darwin": "rbxcs",
        "win32": "rbxcs.exe",
        "special": notact
    },
    "roblox-ts": {
        "repo": "roblox-compilers/roblox-ts",
        "darwin": "rbxtsc",
        "win32": "rbxtsc.exe",
        "special": qts,
        "specialin": installrbxts
    },
    "roblox-kt": {
        "repo": "roblox-compilers/roblox-kt",
        "darwin": "rbxkt",
        "win32": "rbxkt.exe",
        "special": notact
    },
    "qts": {
        "repo": "roblox-compilers/qts",
        "darwin": "qts",
        "win32": "qts.exe",
        "special": None
    }
}

relative = {
    "rbxpy": "roblox-py",
    "rbxc": "roblox-c",
    "rbxcs": "roblox-cs",
    "rbxts": "roblox-ts",
    "rbxkt": "roblox-kt",
    "qts": "qts",
    "roblox-py": "roblox-py",
    "roblox-c": "roblox-c",
    "roblox-cs": "roblox-cs",
    "roblox-ts": "roblox-ts",
    "roblox-kt": "roblox-kt",
}

def install(pkg):
    if (pkg in relative):
        if exec[relative[pkg]]["special"]:
            exec[relative[pkg]]["special"]()
        if "specialin" in exec[relative[pkg]]:
            exec[relative[pkg]]["specialin"]()
        else:
            path = f"https://github.com/{exec[relative[pkg]]['repo']}/releases/latest/download/{exec[relative[pkg]][sys.platform] or log.error('platform not supported')}"
            log.info(f"downloading {pkg}...")
            os.system(f"curl -L {path} -o {exec[relative[pkg]][sys.platform]} > /dev/null 2>&1")
            log.info(f"installing {pkg}...")
            bin(exec[relative[pkg]][sys.platform])
            
    else:
        log.error(f"package '{pkg}' not found")
            
            
def bin(file):
    # Move the file to /usr/bin in macOS and Linux, and to C:\win32dows\System32 in windows
    if sys.platform == "win32":
        os.system(f"move {file} C:\\windows\\System32")
    else:
        os.system(f"chmod +x {file}")
        os.system(f"mv {file} /usr/local/bin")