import json

dict = {
    "Routers": {
        "R1": {
            "Router ID": "1.1.1.1",
            "AS": "111",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:12:12:12::1",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:13:13:13::1",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::1",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["GigabitEthernet1/0","GigabitEthernet2/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {
                        "2001::2": "111",
                        "2001::3": "111",
                        "2001::4": "111",
                        "2001::5": "111",
                        "2001::6": "111",
                        "2001::7": "111"
                    },
                    "Advertise":[
                    ]                   
                }
            }
        },
        "R2": {
            "Router ID": "2.2.2.2",
            "AS": "111",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:12:12:12::2",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:23:23:23::2",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:24:24:24::2",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::2",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["GigabitEthernet1/0", "GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {
                        "2001::1": "111",
                        "2001::3": "111",
                        "2001::4": "111",
                        "2001::5": "111",
                        "2001::6": "111",
                        "2001::7": "111"
                    },
                    "Advertise":[
                    ]                   
                }
            }
        },
        "R3": {
            "Router ID": "3.3.3.3",
            "AS": "111",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:13:13:13::3",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:23:23:23::3",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:35:35:35::3",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::3",
                    "Mask": "128"
                }             
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["GigabitEthernet1/0", "GigabitEthernet2/0", "GigabitEthernet3/0", "Loopback 0"],                    
                },
                "BGP": {
                    "Neighbors": {
                        "2001::1": "111",
                        "2001::2": "111",
                        "2001::4": "111",
                        "2001::5": "111",
                        "2001::6": "111",
                        "2001::7": "111"
                    },
                    "Advertise":[
                    ]                   
                }
            }
        },
        "R4": {
            "Router ID": "4.4.4.4",
            "AS": "111",
            "Interfaces": {
                "FastEthernet0/0": {
                    "IP": "2001:46:46:46::4",
                    "Mask": "64"
                },
                "GigabitEthernet1/0": {
                    "IP": "2001:24:24:24::4",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:45:45:45::4",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:47:47:47::4",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::4",
                    "Mask": "128"
                }             
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["FastEthernet0/0","GigabitEthernet1/0","GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"],
                },
                "BGP": {
                    "Neighbors": {
                        "2001::1": "111",
                        "2001::2": "111",
                        "2001::3": "111",
                        "2001::5": "111",
                        "2001::6": "111",
                        "2001::7": "111"
                    },
                    "Advertise":[
                    ]                   
                }
            }
        },
        "R5": {
            "Router ID": "5.5.5.5",
            "AS": "111",
            "Interfaces": {
                "FastEthernet0/0": {
                    "IP": "2001:57:57:57::5",
                    "Mask": "64"
                },
                "GigabitEthernet1/0": {
                    "IP": "2001:35:35:35::5",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:45:45:45::5",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:56:56:56::5",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::5",
                    "Mask": "128"
                }             
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["FastEthernet0/0","GigabitEthernet1/0","GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"],
                },
                "BGP": {
                    "Neighbors": {
                        "2001::1": "111",
                        "2001::2": "111",
                        "2001::3": "111",
                        "2001::4": "111",
                        "2001::6": "111",
                        "2001::7": "111"
                    },
                    "Advertise":[
                    ]                   
                }
            }
        },
        "R6": {
            "Router ID": "6.6.6.6",
            "AS": "111",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:56:56:56::6",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:46:46:46::6",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:69:69:69::6",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::6",
                    "Mask": "128"
                }             
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["GigabitEthernet1/0","GigabitEthernet2/0", "Loopback 0"],
                    "Redistribute":["connected","bgp 111"]
                },
                "BGP": {
                    "Neighbors": {
                        "2001::1": "111",
                        "2001::2": "111",
                        "2001::3": "111",
                        "2001::4": "111",
                        "2001::5": "111",
                        "2001::7": "111",
                        "2001:69:69:69::9": "112"
                    },
                    "Advertise":[
                        "2001::1/128",
                        "2001::2/128",
                        "2001::3/128",
                        "2001::4/128",
                        "2001::5/128",
                        "2001::7/128",
                        "2001:12:12:12::/64",
                        "2001:13:13:13::/64",
                        "2001:23:23:23::/64",
                        "2001:24:24:24::/64",
                        "2001:35:35:35::/64",
                        "2001:45:45:45::/64",
                        "2001:46:46:46::/64",
                        "2001:47:47:47::/64",
                        "2001:57:57:57::/64",
                        "2001:56:56:56::/64"
                    ]                   
                }
            }
        },
        "R7": {
            "Router ID": "7.7.7.7",
            "AS": "111",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:47:47:47::7",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:57:57:57::7",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:78:78:78::7",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::7",
                    "Mask": "128"
                }             
            },
            "Protocols": {
                "RIP": {
                    "Name": "RIP1",
                    "Interfaces": ["GigabitEthernet1/0","GigabitEthernet2/0", "Loopback 0"],
                    "Redistribute":["connected","bgp 111"]
                },
                "BGP": {
                    "Neighbors": {
                        "2001::1": "111",
                        "2001::2": "111",
                        "2001::3": "111",
                        "2001::4": "111",
                        "2001::5": "111",
                        "2001::6": "111",
                        "2001:78:78:78::8":"112"
                    },
                    "Advertise":[
                        "2001::1/128",
                        "2001::2/128",
                        "2001::3/128",
                        "2001::4/128",
                        "2001::5/128",
                        "2001::6/128",
                        "2001:12:12:12::/64",
                        "2001:13:13:13::/64",
                        "2001:23:23:23::/64",
                        "2001:24:24:24::/64",
                        "2001:35:35:35::/64",
                        "2001:45:45:45::/64",
                        "2001:46:46:46::/64",
                        "2001:47:47:47::/64",
                        "2001:57:57:57::/64",
                        "2001:56:56:56::/64",
                        "2001:78:78:78::/64"
                    ]                   
                }
            }
        },
        "R8": {
            "Router ID": "8.8.8.8",
            "AS": "112",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:78:78:78::8",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:810:810:810::8",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:811:811:811::8",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::8",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Interfaces": ["GigabitEthernet2/0", "GigabitEthernet3/0", "Loopback 0"],
                    "Area": "0",
                    "Redistribute":["connected","bgp 112"]
                },
                "BGP": {
                    "Neighbors": {
                        "2001:78:78:78::7":"111",                        
                        "2001::9": "112",
                        "2001::10": "112",
                        "2001::11": "112",
                        "2001::12": "112",
                        "2001::13": "112",
                        "2001::14": "112"
                    },
                    "Advertise":[
                        "2001:810:810:810::/64",
                        "2001:811:811:811::/64",
                        "2001:910:910:910::/64",
                        "2001:911:911:911::/64",
                        "2001:1011:1011:1011::/64",
                        "2001:1012:1012:1012::/64",
                        "2001:1113:1113:1113::/64",
                        "2001:1213:1213:1213::/64",
                        "2001:1214:1214:1214::/64",
                        "2001:1314:1314:1314::/64",
                        "2001::9/128",
                        "2001::10/128",
                        "2001::11/128",
                        "2001::12/128",
                        "2001::13/128",
                        "2001::14/128",
                    ]
                }
            }
        },
        "R9": {
            "Router ID": "9.9.9.9",
            "AS": "112",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:69:69:69::9",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:911:911:911::9",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:910:910:910::9",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::9",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Area": "0",
                    "Interfaces": ["GigabitEthernet2/0", "GigabitEthernet3/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {                        
                        "2001:69:69:69::6":"111",                        
                        "2001::8": "112",
                        "2001::10": "112",
                        "2001::11": "112",
                        "2001::12": "112",
                        "2001::13": "112",
                        "2001::14": "112"
                    },
                    "Advertise":[
                        "2001:810:810:810::/64",
                        "2001:811:811:811::/64",
                        "2001:910:910:910::/64",
                        "2001:911:911:911::/64",
                        "2001:1011:1011:1011::/64",
                        "2001:1012:1012:1012::/64",
                        "2001:1113:1113:1113::/64",
                        "2001:1213:1213:1213::/64",
                        "2001:1214:1214:1214::/64",
                        "2001:1314:1314:1314::/64",
                        "2001::8/128",
                        "2001::10/128",
                        "2001::11/128",
                        "2001::12/128",
                        "2001::13/128",
                        "2001::14/128",
                    ]
                }
            }
        },
        "R10": {
            "Router ID": "10.10.10.10",
            "AS": "112",
            "Interfaces": {
                "FastEthernet0/0": {
                    "IP": "2001:1011:1011:1011::10",
                    "Mask": "64"
                },
                "GigabitEthernet1/0": {
                    "IP": "2001:810:810:810::10",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:910:910:910::10",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:1012:1012:1012::10",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::10",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Area": "0",
                    "Interfaces": ["FastEthernet0/0", "GigabitEthernet1/0","GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {                        
                        "2001::8": "112",
                        "2001::9": "112",
                        "2001::11": "112",
                        "2001::12": "112",
                        "2001::13": "112",
                        "2001::14": "112"
                    },
                    "Advertise":[
                    ]
                }
            }
        },
        "R11": {
            "Router ID": "11.11.11.11",
            "AS": "112",
            "Interfaces": {
                "FastEthernet0/0": {
                    "IP": "2001:1011:1011:1011::11",
                    "Mask": "64"
                },
                "GigabitEthernet1/0": {
                    "IP": "2001:911:911:911::11",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:811:811:811::11",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:1113:1113:1113::11",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::11",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Area": "0",
                    "Interfaces": ["FastEthernet0/0", "GigabitEthernet1/0","GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {                        
                        "2001::8": "112",
                        "2001::9": "112",
                        "2001::10": "112",
                        "2001::12": "112",
                        "2001::13": "112",
                        "2001::14": "112"

                    },
                    "Advertise":[
                    ]
                }
            }
        },
        "R12": {
            "Router ID": "12.12.12.12",
            "AS": "112",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:1012:1012:1012::12",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:1213:1213:1213::12",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:1214:1214:1214::12",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::12",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Area": "0",
                    "Interfaces": ["GigabitEthernet1/0","GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {                        
                        "2001::8": "112",
                        "2001::9": "112",
                        "2001::10": "112",
                        "2001::11": "112",
                        "2001::13": "112",
                        "2001::14": "112"
                    },
                    "Advertise":[
                    ]
                }
            }
        },
        "R13": {
            "Router ID": "13.13.13.13",
            "AS": "112",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:1113:1113:1113::13",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:1213:1213:1213::13",
                    "Mask": "64"
                },
                "GigabitEthernet3/0": {
                    "IP": "2001:1314:1314:1314::13",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::13",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Area": "0",
                    "Interfaces": ["GigabitEthernet1/0","GigabitEthernet2/0","GigabitEthernet3/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {                        
                        "2001::8": "112",
                        "2001::9": "112",
                        "2001::10": "112",
                        "2001::11": "112",
                        "2001::12": "112",
                        "2001::14": "112"
                    },
                    "Advertise":[
                    ]
                }
            }
        },
        "R14": {
            "Router ID": "14.14.14.14",
            "AS": "112",
            "Interfaces": {
                "GigabitEthernet1/0": {
                    "IP": "2001:1314:1314:1314::14",
                    "Mask": "64"
                },
                "GigabitEthernet2/0": {
                    "IP": "2001:1214:1214:1214::14",
                    "Mask": "64"
                },
                "Loopback 0": {
                    "IP": "2001::14",
                    "Mask": "128"
                }
            },
            "Protocols": {
                "OSPF": {
                    "Name": "2",
                    "Area": "0",
                    "Interfaces": ["GigabitEthernet1/0","GigabitEthernet2/0", "Loopback 0"]
                },
                "BGP": {
                    "Neighbors": {                        
                        "2001::8": "112",
                        "2001::9": "112",
                        "2001::10": "112",
                        "2001::11": "112",
                        "2001::12": "112",
                        "2001::13": "112"
                    },
                    "Advertise":[
                    ]
                }
            }
        }                    
    }
}

# Créer le fichier JSON à partir du dictionnaire
with open('routers_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dict, json_file, indent=4, ensure_ascii=False)

print("Le fichier JSON a été créé avec succès.")