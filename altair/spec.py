SPEC = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Schema for Vega-lite specification",
    "type": "object",
    "required": ["marktype","encoding","data"],
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "formatType": {"type": "string",
                               "enum": ["json","csv"],"default": "json"},
                "url": {"type": "string"},
                "values": {
                    "type": "array",
                    "description": "Pass array of objects instead of a url to a file.",
                    "items": {"type": "object",
                              "additionalProperties": True}
                    }
            }
        },
        "marktype": {
            "type": "string",
            "enum": ["point","tick","bar","line","area","circle","square","text"]
        },
        "encoding": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string",
                                 "enum": ["N","O","Q","T"]
                                },
                        "aggregate": {
                            "type": "string",
                            "enum": ["avg","sum","median","min","max","count"],
                            "supportedEnums": {
                                "Q": ["avg","median","sum","min","max","count"],
                                "O": ["median","min","max"],
                                "N": [],
                                "T": ["avg","median","min","max"],
                                "": ["count"]
                            },
                            "supportedTypes": {"Q": 1,"N": 1,"O": 1,"T": 1,"": 1}
                        },
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "scale": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["linear","log","pow","sqrt","quantile"],
                                    "default": "linear",
                                    "supportedTypes": {"Q": 1}
                                },
                                "reverse": {"type": "boolean","default": False,"supportedTypes": {"Q": 1,"T": 1}},
                                "zero": {
                                    "type": "boolean",
                                    "description": "Include zero",
                                    "default": True,
                                    "supportedTypes": {"Q": 1,"T": 1}
                                },
                                "nice": {
                                    "type": "string",
                                    "enum": ["second","minute","hour","day","week","month","year"],
                                    "supportedTypes": {"T": 1}
                                },
                                "useRawDomain": {
                                    "type": "boolean",
                                    "description": "Use the raw data range as scale domain instead of aggregated data for aggregate axis. This option does not work with sum or count aggregateas they might have a substantially larger scale range.By default, use value from config.useRawDomain."
                                }
                            }
                        },
                        "axis": {
                            "type": "object",
                            "properties": {
                                "grid": {
                                    "type": "boolean",
                                    "default": True,
                                    "description": "A flag indicate if gridlines should be created in addition to ticks."
                                },
                                "layer": {
                                    "type": "string",
                                    "default": "back",
                                    "description": "A string indicating if the axis (and any gridlines) should be placed above or below the data marks."
                                },
                                "orient": {
                                    "type": "string",
                                    "enum": ["top","right","left","bottom"],
                                    "description": "The orientation of the axis. One of top, bottom, left or right. The orientation can be used to further specialize the axis type (e.g., a y axis oriented for the right edge of the chart)."
                                },
                                "ticks": {
                                    "type": "integer",
                                    "default": 5,
                                    "description": "A desired number of ticks, for axes visualizing quantitative scales. The resulting number may be different so that values are \"nice\" (multiples of 2, 5, 10) and lie within the underlying scale's range."
                                },
                                "title": {
                                    "type": "string",
                                    "description": "A title for the axis. (Shows field name and its function by default.)"
                                },
                                "titleMaxLength": {
                                    "type": "integer",
                                    "description": "Max length for axis title if the title is automatically generated from the field's description"
                                },
                                "titleOffset": {"type": "integer","description": "A title offset value for the axis."},
                                "format": {
                                    "type": "string",
                                    "description": "The formatting pattern for axis labels. If not undefined, this will be determined by small/largeNumberFormat and the max value of the field."
                                },
                                "maxLabelLength": {
                                    "type": "integer",
                                    "default": 25,
                                    "minimum": 0,
                                    "description": "Truncate labels that are too long."
                                }
                            }
                        },
                        "band": {
                            "type": "object",
                            "properties": {
                                "size": {"type": "integer",
                                         "minimum": 0},
                                "padding": {"type": "integer",
                                            "minimum": 0,
                                            "default": 1}
                            }
                        },
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string",
                                                  "enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean",
                                                "default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"measure": True,"dimension": True},
                    "supportedMarktypes": {
                        "point": True,
                        "tick": True,
                        "bar": True,
                        "line": True,
                        "area": True,
                        "circle": True,
                        "square": True
                    },
                    "required": ["name","type"]
                },
                "y": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "aggregate": {
                            "type": "string",
                            "enum": ["avg","sum","median","min","max","count"],
                            "supportedEnums": {
                                "Q": ["avg","median","sum","min","max","count"],
                                "O": ["median","min","max"],
                                "N": [],
                                "T": ["avg","median","min","max"],
                                "": ["count"]
                            },
                            "supportedTypes": {"Q": 1,"N": 1,"O": 1,"T": 1,"": 1}
                        },
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "scale": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["linear","log","pow","sqrt","quantile"],
                                    "default": "linear",
                                    "supportedTypes": {"Q": 1}
                                },
                                "reverse": {"type": "boolean","default": False,"supportedTypes": {"Q": 1,"T": 1}},
                                "zero": {
                                    "type": "boolean",
                                    "description": "Include zero",
                                    "default": True,
                                    "supportedTypes": {"Q": 1,"T": 1}
                                },
                                "nice": {
                                    "type": "string",
                                    "enum": ["second","minute","hour","day","week","month","year"],
                                    "supportedTypes": {"T": 1}
                                },
                                "useRawDomain": {
                                    "type": "boolean",
                                    "description": "Use the raw data range as scale domain instead of aggregated data for aggregate axis. This option does not work with sum or count aggregateas they might have a substantially larger scale range.By default, use value from config.useRawDomain."
                                }
                            }
                        },
                        "axis": {
                            "type": "object",
                            "properties": {
                                "grid": {
                                    "type": "boolean",
                                    "default": True,
                                    "description": "A flag indicate if gridlines should be created in addition to ticks."
                                },
                                "layer": {
                                    "type": "string",
                                    "default": "back",
                                    "description": "A string indicating if the axis (and any gridlines) should be placed above or below the data marks."
                                },
                                "orient": {
                                    "type": "string",
                                    "enum": ["top","right","left","bottom"],
                                    "description": "The orientation of the axis. One of top, bottom, left or right. The orientation can be used to further specialize the axis type (e.g., a y axis oriented for the right edge of the chart)."
                                },
                                "ticks": {
                                    "type": "integer",
                                    "default": 5,
                                    "description": "A desired number of ticks, for axes visualizing quantitative scales. The resulting number may be different so that values are \"nice\" (multiples of 2, 5, 10) and lie within the underlying scale's range."
                                },
                                "title": {
                                    "type": "string",
                                    "description": "A title for the axis. (Shows field name and its function by default.)"
                                },
                                "titleMaxLength": {
                                    "type": "integer",
                                    "description": "Max length for axis title if the title is automatically generated from the field's description"
                                },
                                "titleOffset": {"type": "integer","description": "A title offset value for the axis."},
                                "format": {
                                    "type": "string",
                                    "description": "The formatting pattern for axis labels. If not undefined, this will be determined by small/largeNumberFormat and the max value of the field."
                                },
                                "maxLabelLength": {
                                    "type": "integer",
                                    "default": 25,
                                    "minimum": 0,
                                    "description": "Truncate labels that are too long."
                                }
                            }
                        },
                        "band": {
                            "type": "object",
                            "properties": {
                                "size": {"type": "integer","minimum": 0},
                                "padding": {"type": "integer","minimum": 0,"default": 1}
                            }
                        },
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"measure": True,"dimension": True},
                    "supportedMarktypes": {
                        "point": True,
                        "tick": True,
                        "bar": True,
                        "line": True,
                        "area": True,
                        "circle": True,
                        "square": True
                    },
                    "required": ["name","type"]
                },
                "row": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "aggregate": {"type": "string","enum": ["count"],"supportedTypes": {"N": 1,"O": 1}},
                        "padding": {"type": "number","minimum": 0,"maximum": 1,"default": 0.1},
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        },
                        "axis": {
                            "type": "object",
                            "properties": {
                                "grid": {
                                    "type": "boolean",
                                    "default": True,
                                    "description": "A flag indicate if gridlines should be created in addition to ticks."
                                },
                                "layer": {
                                    "type": "string",
                                    "default": "back",
                                    "description": "A string indicating if the axis (and any gridlines) should be placed above or below the data marks."
                                },
                                "orient": {
                                    "type": "string",
                                    "enum": ["top","right","left","bottom"],
                                    "description": "The orientation of the axis. One of top, bottom, left or right. The orientation can be used to further specialize the axis type (e.g., a y axis oriented for the right edge of the chart)."
                                },
                                "ticks": {
                                    "type": "integer",
                                    "default": 5,
                                    "description": "A desired number of ticks, for axes visualizing quantitative scales. The resulting number may be different so that values are \"nice\" (multiples of 2, 5, 10) and lie within the underlying scale's range."
                                },
                                "title": {
                                    "type": "string",
                                    "description": "A title for the axis. (Shows field name and its function by default.)"
                                },
                                "titleMaxLength": {
                                    "type": "integer",
                                    "description": "Max length for axis title if the title is automatically generated from the field's description"
                                },
                                "titleOffset": {"type": "integer","description": "A title offset value for the axis."},
                                "format": {
                                    "type": "string",
                                    "description": "The formatting pattern for axis labels. If not undefined, this will be determined by small/largeNumberFormat and the max value of the field."
                                },
                                "maxLabelLength": {
                                    "type": "integer",
                                    "default": 25,
                                    "minimum": 0,
                                    "description": "Truncate labels that are too long."
                                }
                            }
                        },
                        "height": {"type": "number","minimum": 0,"default": 150}
                    },
                    "supportedRole": {"dimension": True},
                    "required": ["name","type"],
                    "supportedMarktypes": {
                        "point": True,
                        "tick": True,
                        "bar": True,
                        "line": True,
                        "area": True,
                        "circle": True,
                        "square": True,
                        "text": True
                    }
                },
                "col": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "aggregate": {"type": "string","enum": ["count"],"supportedTypes": {"N": 1,"O": 1}},
                        "padding": {"type": "number","minimum": 0,"maximum": 1,"default": 0.1},
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        },
                        "axis": {
                            "type": "object",
                            "properties": {
                                "grid": {
                                    "type": "boolean",
                                    "default": True,
                                    "description": "A flag indicate if gridlines should be created in addition to ticks."
                                },
                                "layer": {
                                    "type": "string",
                                    "default": "back",
                                    "description": "A string indicating if the axis (and any gridlines) should be placed above or below the data marks."
                                },
                                "orient": {
                                    "type": "string",
                                    "enum": ["top","right","left","bottom"],
                                    "description": "The orientation of the axis. One of top, bottom, left or right. The orientation can be used to further specialize the axis type (e.g., a y axis oriented for the right edge of the chart)."
                                },
                                "ticks": {
                                    "type": "integer",
                                    "default": 5,
                                    "description": "A desired number of ticks, for axes visualizing quantitative scales. The resulting number may be different so that values are \"nice\" (multiples of 2, 5, 10) and lie within the underlying scale's range."
                                },
                                "title": {
                                    "type": "string",
                                    "description": "A title for the axis. (Shows field name and its function by default.)"
                                },
                                "titleMaxLength": {
                                    "type": "integer",
                                    "description": "Max length for axis title if the title is automatically generated from the field's description"
                                },
                                "titleOffset": {"type": "integer","description": "A title offset value for the axis."},
                                "format": {
                                    "type": "string",
                                    "description": "The formatting pattern for axis labels. If not undefined, this will be determined by small/largeNumberFormat and the max value of the field."
                                },
                                "maxLabelLength": {
                                    "type": "integer",
                                    "default": 12,
                                    "minimum": 0,
                                    "description": "Truncate labels that are too long."
                                }
                            }
                        },
                        "width": {"type": "number","minimum": 0,"default": 150}
                    },
                    "supportedRole": {"dimension": True},
                    "required": ["name","type"],
                    "supportedMarktypes": {
                        "point": True,
                        "tick": True,
                        "bar": True,
                        "line": True,
                        "area": True,
                        "circle": True,
                        "square": True,
                        "text": True
                    }
                },
                "size": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "aggregate": {
                            "type": "string",
                            "enum": ["avg","sum","median","min","max","count"],
                            "supportedEnums": {
                                "Q": ["avg","median","sum","min","max","count"],
                                "O": ["median","min","max"],
                                "N": [],
                                "T": ["avg","median","min","max"],
                                "": ["count"]
                            },
                            "supportedTypes": {"Q": 1,"N": 1,"O": 1,"T": 1,"": 1}
                        },
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "scale": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["linear","log","pow","sqrt","quantile"],
                                    "default": "linear",
                                    "supportedTypes": {"Q": 1}
                                },
                                "reverse": {"type": "boolean","default": False,"supportedTypes": {"Q": 1,"T": 1}},
                                "zero": {
                                    "type": "boolean",
                                    "description": "Include zero",
                                    "default": True,
                                    "supportedTypes": {"Q": 1,"T": 1}
                                },
                                "nice": {
                                    "type": "string",
                                    "enum": ["second","minute","hour","day","week","month","year"],
                                    "supportedTypes": {"T": 1}
                                },
                                "useRawDomain": {
                                    "type": "boolean",
                                    "description": "Use the raw data range as scale domain instead of aggregated data for aggregate axis. This option does not work with sum or count aggregateas they might have a substantially larger scale range.By default, use value from config.useRawDomain."
                                }
                            }
                        },
                        "legend": {"type": "boolean","default": True},
                        "value": {"type": "integer","default": 30,"minimum": 0},
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"measure": True,"dimension": "ordinal-only"},
                    "supportedMarktypes": {"point": True,"bar": True,"circle": True,"square": True,"text": True}
                },
                "color": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "aggregate": {
                            "type": "string",
                            "enum": ["avg","sum","median","min","max","count"],
                            "supportedEnums": {
                                "Q": ["avg","median","sum","min","max","count"],
                                "O": ["median","min","max"],
                                "N": [],
                                "T": ["avg","median","min","max"],
                                "": ["count"]
                            },
                            "supportedTypes": {"Q": 1,"N": 1,"O": 1,"T": 1,"": 1}
                        },
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "scale": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["linear","log","pow","sqrt","quantile"],
                                    "default": "linear",
                                    "supportedTypes": {"Q": 1}
                                },
                                "reverse": {"type": "boolean","default": False,"supportedTypes": {"Q": 1,"T": 1}},
                                "zero": {
                                    "type": "boolean",
                                    "description": "Include zero",
                                    "default": True,
                                    "supportedTypes": {"Q": 1,"T": 1}
                                },
                                "nice": {
                                    "type": "string",
                                    "enum": ["second","minute","hour","day","week","month","year"],
                                    "supportedTypes": {"T": 1}
                                },
                                "useRawDomain": {
                                    "type": "boolean",
                                    "description": "Use the raw data range as scale domain instead of aggregated data for aggregate axis. This option does not work with sum or count aggregateas they might have a substantially larger scale range.By default, use value from config.useRawDomain."
                                },
                                "range": {
                                    "type": ["string","array"],
                                    "description": "color palette, if undefined vega-lite will use data propertyto pick one from c10palette, c20palette, or ordinalPalette"
                                },
                                "c10palette": {
                                    "type": "string",
                                    "default": "category10",
                                    "enum": ["category10","category10k","Pastel1","Pastel2","Set1","Set2","Set3"]
                                },
                                "c20palette": {
                                    "type": "string",
                                    "default": "category20",
                                    "enum": ["category20","category20b","category20c"]
                                },
                                "ordinalPalette": {
                                    "type": "string",
                                    "default": "BuGn",
                                    "enum": [
                                        "YlGn",
                                        "YlGnBu",
                                        "GnBu",
                                        "BuGn",
                                        "PuBuGn",
                                        "PuBu",
                                        "BuPu",
                                        "RdPu",
                                        "PuRd",
                                        "OrRd",
                                        "YlOrRd",
                                        "YlOrBr",
                                        "Purples",
                                        "Blues",
                                        "Greens",
                                        "Oranges",
                                        "Reds",
                                        "Greys",
                                        "PuOr",
                                        "BrBG",
                                        "PRGn",
                                        "PiYG",
                                        "RdBu",
                                        "RdGy",
                                        "RdYlBu",
                                        "Spectral",
                                        "RdYlGn",
                                        "Accent",
                                        "Dark2",
                                        "Paired",
                                        "Pastel1",
                                        "Pastel2",
                                        "Set1",
                                        "Set2",
                                        "Set3"
                                    ]
                                }
                            }
                        },
                        "legend": {"type": "boolean","default": True},
                        "value": {"type": "string","role": "color","default": "steelblue"},
                        "opacity": {"type": "number","minimum": 0,"maximum": 1},
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"measure": True,"dimension": True},
                    "supportedMarktypes": {
                        "point": True,
                        "tick": True,
                        "bar": True,
                        "line": True,
                        "area": True,
                        "circle": True,
                        "square": True,
                        "text": True
                    }
                },
                "shape": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "aggregate": {"type": "string","enum": ["count"],"supportedTypes": {"N": 1,"O": 1}},
                        "legend": {"type": "boolean","default": True},
                        "value": {
                            "type": "string",
                            "enum": ["circle","square","cross","diamond","triangle-up","triangle-down"],
                            "default": "circle"
                        },
                        "filled": {
                            "type": "boolean",
                            "default": False,
                            "description": "whether the shape's color should be used as fill color instead of stroke color"
                        },
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"dimension": True},
                    "supportedMarktypes": {"point": True,"circle": True,"square": True}
                },
                "text": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "aggregate": {
                            "type": "string",
                            "enum": ["avg","sum","median","min","max","count"],
                            "supportedEnums": {
                                "Q": ["avg","median","sum","min","max","count"],
                                "O": ["median","min","max"],
                                "N": [],
                                "T": ["avg","median","min","max"],
                                "": ["count"]
                            },
                            "supportedTypes": {"Q": 1,"N": 1,"O": 1,"T": 1,"": 1}
                        },
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "scale": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["linear","log","pow","sqrt","quantile"],
                                    "default": "linear",
                                    "supportedTypes": {"Q": 1}
                                },
                                "reverse": {"type": "boolean","default": False,"supportedTypes": {"Q": 1,"T": 1}},
                                "zero": {
                                    "type": "boolean",
                                    "description": "Include zero",
                                    "default": True,
                                    "supportedTypes": {"Q": 1,"T": 1}
                                },
                                "nice": {
                                    "type": "string",
                                    "enum": ["second","minute","hour","day","week","month","year"],
                                    "supportedTypes": {"T": 1}
                                },
                                "useRawDomain": {
                                    "type": "boolean",
                                    "description": "Use the raw data range as scale domain instead of aggregated data for aggregate axis. This option does not work with sum or count aggregateas they might have a substantially larger scale range.By default, use value from config.useRawDomain."
                                }
                            }
                        },
                        "align": {"type": "string","default": "right"},
                        "baseline": {"type": "string","default": "middle"},
                        "color": {"type": "string","role": "color","default": "#000000"},
                        "margin": {"type": "integer","default": 4,"minimum": 0},
                        "placeholder": {"type": "string","default": "Abc"},
                        "font": {
                            "type": "object",
                            "properties": {
                                "weight": {"type": "string","enum": ["normal","bold"],"default": "normal"},
                                "size": {"type": "integer","default": 10,"minimum": 0},
                                "family": {"type": "string","default": "Helvetica Neue"},
                                "style": {"type": "string","default": "normal","enum": ["normal","italic"]}
                            }
                        },
                        "format": {
                            "type": "string",
                            "description": "The formatting pattern for text value. If not undefined, this will be determined by small/largeNumberFormat and the max value of the field."
                        },
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"measure": True},
                    "supportedMarktypes": {"text": True}
                },
                "detail": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "type": {"type": "string","enum": ["N","O","Q","T"]},
                        "timeUnit": {
                            "type": "string",
                            "enum": ["year","month","day","date","hours","minutes","seconds"],
                            "supportedTypes": {"T": 1}
                        },
                        "bin": {
                            "type": ["boolean","object"],
                            "default": False,
                            "properties": {
                                "maxbins": {
                                    "type": "integer",
                                    "default": 15,
                                    "minimum": 2,
                                    "description": "Maximum number of bins."
                                }
                            },
                            "supportedTypes": {"Q": 1}
                        },
                        "aggregate": {"type": "string","enum": ["count"],"supportedTypes": {"N": 1,"O": 1}},
                        "sort": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "type": "object",
                                "supportedTypes": {"N": 1,"O": 1},
                                "required": ["name","aggregate"],
                                "properties": {
                                    "name": {"type": "string"},
                                    "aggregate": {"type": "string","enum": ["avg","sum","min","max","count"]},
                                    "reverse": {"type": "boolean","default": False}
                                }
                            }
                        }
                    },
                    "supportedRole": {"dimension": True},
                    "supportedMarktypes": {"point": True,"tick": True,"line": True,"circle": True,"square": True}
                }
            }
        },
        "filter": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "operands": {"type": "array",
                                 "items": {
                                     "type": ["string",
                                              "boolean",
                                              "integer",
                                              "number"]
                                 }
                                },
                    "operator": {"type": "string",
                                 "enum": [">",">=","=","!=","<","<=","notNull"]
                                }
                }
            }
        },
        "config": {
            "type": "object",
            "properties": {
                "width": {"type": "integer"},
                "height": {"type": "integer"},
                "viewport": {"type": "array","items": {"type": "integer"}},
                "gridColor": {"type": "string","role": "color","default": "black"},
                "gridOpacity": {"type": "number","minimum": 0,"maximum": 1,"default": 0.08},
                "filterNull": {
                    "type": "object",
                    "properties": {
                        "O": {"type": "boolean","default": False},
                        "Q": {"type": "boolean","default": True},
                        "T": {"type": "boolean","default": True}
                    }
                },
                "toggleSort": {"type": "string","default": "O"},
                "singleHeight": {"type": "integer","default": 200,"minimum": 0},
                "singleWidth": {"type": "integer","default": 200,"minimum": 0},
                "largeBandSize": {"type": "integer","default": 21,"minimum": 0},
                "smallBandSize": {"type": "integer","default": 12,"minimum": 0},
                "largeBandMaxCardinality": {"type": "integer","default": 10},
                "cellPadding": {"type": "number","default": 0.1},
                "cellGridColor": {"type": "string","role": "color","default": "black"},
                "cellGridOpacity": {"type": "number","minimum": 0,"maximum": 1,"default": 0.15},
                "cellBackgroundColor": {"type": "string","role": "color","default": "transparent"},
                "textCellWidth": {"type": "integer","default": 90,"minimum": 0},
                "strokeWidth": {"type": "integer","default": 2,"minimum": 0},
                "singleBarOffset": {"type": "integer","default": 5,"minimum": 0},
                "timeScaleLabelLength": {
                    "type": "integer",
                    "default": 3,
                    "minimum": 0,
                    "description": "Max length for values in dayScaleLabel and monthScaleLabel.  Zero means using full names in dayScaleLabel/monthScaleLabel."
                },
                "dayScaleLabel": {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                    "description": "Axis labels for day of week, starting from Sunday.(Consistent with Javascript -- See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay."
                },
                "monthScaleLabel": {
                    "type": "array",
                    "items": {"type": "string"},
                    "default": [
                        "January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"
                    ],
                    "description": "Axis labels for month."
                },
                "characterWidth": {"type": "integer","default": 6},
                "maxSmallNumber": {
                    "type": "number",
                    "default": 10000,
                    "description": "maximum number that a field will be considered smallNumber.Used for axis labelling."
                },
                "smallNumberFormat": {
                    "type": "string",
                    "default": "",
                    "description": "D3 Number format for axis labels and text tables for number <= maxSmallNumber. Used for axis labelling."
                },
                "largeNumberFormat": {
                    "type": "string",
                    "default": ".3s",
                    "description": "D3 Number format for axis labels and text tables for number > maxSmallNumber."
                },
                "timeFormat": {
                    "type": "string",
                    "default": "%Y-%m-%d",
                    "description": "Date format for axis labels."
                },
                "useRawDomain": {
                    "type": "boolean",
                    "default": False,
                    "description": "Use the raw data range as scale domain instead of aggregated data for aggregate axis. This option does not work with sum or count aggregateas they might have a substantially larger scale range.By default, use value from config.useRawDomain."
                }
            }
        }
    }
}
