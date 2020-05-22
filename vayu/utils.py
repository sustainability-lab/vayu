class Legend:
    """Utility class for getting AQ standards.
  """

    import numpy as np
    import branca.colormap as cm

    country_pollutants = {
        "Canada": {
            "AQHI": {
                "notation": "Air Quality Health Index",
                "bin_edges": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]),
                "color_scale": np.array(
                    [
                        "#00ccff",
                        "#0099cc",
                        "#006699",
                        "#ffff00",
                        "#ffcc00",
                        "#ff9933",
                        "#ff6666",
                        "#ff0000",
                        "#cc0000",
                        "#990000",
                        "#660000",
                    ]
                ),
            }
        },
        "Hong Kong": {
            "AQHI": {
                "notation": "Air Quality Health Index",
                "bin_edges": np.array([3, 6, 7, 10, 20]),
                "color_scale": np.array(
                    ["#008000", "#FFA500", "#FF0000", "#A52A2A", "#000000"]
                ),
            }
        },
        "Mainland China": {
            "AQI": {
                "notation": "Air Quality Index",
                "bin_edges": np.array([50, 100, 150, 200, 300, 450]),
                "color_scale": np.array(
                    ["#00FF00", "#FFFF00", "#FF9900", "#FF0000", "#540099", "#800000"]
                ),
            }
        },
        "South Korea": {
            "CAI": {
                "notation": "Comprehensive Air-quality Index",
                "bin_edges": np.array([50, 100, 150, 200, 350, 500]),
                "color_scale": np.array(
                    ["#0000FF", "#005500", "#FFFF00", "#FF9900", "#FF0000", "#990000"]
                ),
            }
        },
        "United Kingdom": {
            "APB": {
                "notation": "Air Pollution Banding",
                "bin_edges": np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                "color_scale": np.array(
                    [
                        "#CCFFCC",
                        "#66FF66",
                        "#00FF00",
                        "#99FF00",
                        "#FFFF00",
                        "#FFCC00",
                        "#FF6600",
                        "#FF3300",
                        "#FF0000",
                        "#FF0066",
                    ]
                ),
            }
        },
        "India": {
            "AQI": {
                "notation": "Air Quality Index",
                "bin_edges": np.array([50, 100, 200, 300, 400, 500]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "so2": {
                "notation": "Sulphur dioxide",
                "bin_edges": np.array([40, 80, 380, 800, 1600]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "pm10": {
                "notation": "Particulate matter < 10 µm",
                "bin_edges": np.array([50, 100, 250, 350, 430]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "pm25": {
                "notation": "Particulate matter < 2.5 µm",
                "bin_edges": np.array([30, 60, 90, 120, 250]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "o3": {
                "notation": "Ozone",
                "bin_edges": np.array([50, 100, 168, 208, 748]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "no2": {
                "notation": "Nitrogen Dioxide",
                "bin_edges": np.array([40, 80, 180, 280, 400]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "co": {
                "notation": "Carbon Monoxide",
                "bin_edges": np.array([1, 2, 10, 17, 34]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "nh3": {
                "notation": "Ammonia",
                "bin_edges": np.array([200, 400, 800, 1200, 1800]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
            "pb": {
                "notation": "Lead",
                "bin_edges": np.array([0.5, 1, 2, 3, 3.5]),
                "color_scale": np.array(
                    ["#00CC00", "#66CC00", "#FFFF00", "#FF9900", "#FF0000", "#A52A2A"]
                ),
            },
        },
        "Europe": {
            "CAQI": {
                "notation": "Common Air Quality Index (CAQI)",
                "bin_edges": np.array([25, 50, 75, 100, 200]),
                "color_scale": np.array(
                    ["#79BC6A", "#BBCF4C", "#EEC20B", "#F29305", "#E8416F"]
                ),
            }
        },
        "USA": {
            "AQI": {
                "notation": "Air Quality Index",
                "bin_edges": np.array([50, 100, 150, 200, 300, 500]),
                "color_scale": np.array(
                    ["#00E400", "#FFFF00", "#FF7E00", "#FF0000", "#99004C", "#7E0023"]
                ),
            }
        },
    }

    def pollutant_legend(country, pollutant):
        colormap = Legend.cm.LinearColormap(
            colors=Legend.country_pollutants[country][pollutant]["color_scale"],
            vmin=0,
            vmax=Legend.country_pollutants[country][pollutant]["bin_edges"][-1],
            index=Legend.country_pollutants[country][pollutant]["bin_edges"],
        )
        return colormap

    def pollutant_color_coding(poll, country, pollutant):
        bin_edges = Legend.country_pollutants[country][pollutant]["bin_edges"]
        idx = np.digitize(poll, bin_edges, right=True)
        return Legend.country_pollutants[country][pollutant]["color_scale"][idx]
