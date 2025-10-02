"""
Regional climate impact data and adaptation strategies for the Climate Futures Storyteller.
Contains specific information about how climate change affects different regions globally.
"""

REGIONAL_CLIMATE_DATA = {
    "coastal_regions": {
        "miami_florida": {
            "climate_impacts": [
                "sea_level_rise",
                "increased_hurricane_intensity",
                "saltwater_intrusion",
                "urban_flooding",
                "beach_erosion",
            ],
            "specific_details": {
                "sea_level_rise": "6-12 inches by 2030, 1-2 feet by 2050",
                "flooding_frequency": "High-tide flooding 10x more frequent than 2020",
                "adaptation_strategies": [
                    "elevated_buildings",
                    "flood_barriers",
                    "living_shorelines",
                    "stormwater_management",
                ],
                "economic_impact": "Property values declining in flood-prone areas",
                "community_response": "Mixed - some residents adapting, others relocating",
            },
            "cultural_context": "Strong community ties, tourism-dependent economy, diverse population",
        },
        "bangladesh_delta": {
            "climate_impacts": [
                "sea_level_rise",
                "cyclone_intensification",
                "saltwater_intrusion",
                "river_flooding",
                "displacement",
            ],
            "specific_details": {
                "sea_level_rise": "1-3 feet by 2050",
                "displacement_estimate": "13 million people by 2050",
                "adaptation_strategies": [
                    "floating_gardens",
                    "cyclone_shelters",
                    "mangrove_restoration",
                    "community_early_warning",
                ],
                "economic_impact": "Agricultural land becoming saline, fishing patterns changing",
                "community_response": "Strong community resilience, traditional adaptation knowledge",
            },
            "cultural_context": "Deep connection to land, strong community networks, traditional knowledge",
        },
    },
    "arid_regions": {
        "southwestern_usa": {
            "climate_impacts": [
                "prolonged_drought",
                "water_scarcity",
                "wildfire_increase",
                "heat_waves",
                "agricultural_challenges",
            ],
            "specific_details": {
                "temperature_increase": "2-4°F by 2050",
                "precipitation_decrease": "10-20% reduction",
                "adaptation_strategies": [
                    "water_conservation",
                    "drought_resistant_crops",
                    "solar_power",
                    "xeriscaping",
                ],
                "economic_impact": "Water rights conflicts, agricultural adaptation costs",
                "community_response": "Innovation in water management, community gardens",
            },
            "cultural_context": "Water rights history, desert adaptation traditions, growing urban populations",
        },
        "sahel_africa": {
            "climate_impacts": [
                "desertification",
                "irregular_rainfall",
                "food_insecurity",
                "conflict_over_resources",
                "migration",
            ],
            "specific_details": {
                "rainfall_variability": "Increased unpredictability",
                "temperature_increase": "1.5-2°C by 2050",
                "adaptation_strategies": [
                    "agroforestry",
                    "water_harvesting",
                    "drought_resistant_crops",
                    "community_networks",
                ],
                "economic_impact": "Livelihood diversification, migration patterns",
                "community_response": "Traditional knowledge integration, community cooperation",
            },
            "cultural_context": "Nomadic traditions, strong community bonds, resource sharing",
        },
    },
    "mountain_regions": {
        "himalayas": {
            "climate_impacts": [
                "glacier_melting",
                "changing_precipitation",
                "landslides",
                "water_scarcity",
                "ecosystem_shifts",
            ],
            "specific_details": {
                "glacier_loss": "1/3 of glaciers lost by 2050",
                "temperature_increase": "1-2°C by 2050",
                "adaptation_strategies": [
                    "terrace_farming",
                    "water_storage",
                    "ecotourism",
                    "renewable_energy",
                ],
                "economic_impact": "Hydroelectric power changes, tourism adaptation",
                "community_response": "Traditional knowledge preservation, community water management",
            },
            "cultural_context": "Sacred mountain traditions, water as life source, community interdependence",
        }
    },
    "urban_centers": {
        "new_york_city": {
            "climate_impacts": [
                "urban_heat_island",
                "flooding_events",
                "infrastructure_stress",
                "air_quality_issues",
                "energy_demands",
            ],
            "specific_details": {
                "temperature_increase": "3-5°F above surrounding areas",
                "flooding_risk": "100-year flood every 3-5 years by 2050",
                "adaptation_strategies": [
                    "green_roofs",
                    "flood_barriers",
                    "cooling_centers",
                    "renewable_energy",
                ],
                "economic_impact": "Infrastructure adaptation costs, property value shifts",
                "community_response": "Community resilience networks, environmental justice focus",
            },
            "cultural_context": "Diverse neighborhoods, strong community organizations, innovation culture",
        }
    },
}

CLIMATE_IMPACT_DESCRIPTIONS = {
    "sea_level_rise": {
        "sensory_details": "The sound of water lapping against new boundaries, the smell of salt in unexpected places, the sight of familiar landmarks slowly disappearing beneath the waves",
        "daily_changes": "Commuting routes that now require boats, homes that need regular pumping, gardens that must be elevated or abandoned",
        "emotional_impact": "A sense of loss mixed with determination, the strange beauty of adaptation",
    },
    "drought": {
        "sensory_details": "The crack of parched earth, the weight of water restrictions, the dust that seems to coat everything",
        "daily_changes": "Shorter showers, brown lawns, different shopping patterns, new ways of growing food",
        "emotional_impact": "Anxiety about resources, pride in conservation, community solidarity",
    },
    "extreme_heat": {
        "sensory_details": "The oppressive weight of air that feels like a blanket, the relief of shade, the constant hum of cooling systems",
        "daily_changes": "Shifted work hours, indoor activities, different clothing choices, new social patterns",
        "emotional_impact": "Exhaustion, adaptation, finding new rhythms",
    },
    "wildfire": {
        "sensory_details": "The acrid smell of smoke, the orange glow of distant flames, the ash that falls like snow",
        "daily_changes": "Evacuation bags always ready, different outdoor activities, new insurance concerns",
        "emotional_impact": "Constant vigilance, community support, resilience in the face of loss",
    },
}

CHARACTER_TEMPLATES = {
    "coastal_community": {
        "professions": [
            "fisherman",
            "tourism_worker",
            "small_business_owner",
            "teacher",
            "elderly_retiree",
        ],
        "ages": ["young_adult", "middle_aged", "elderly"],
        "backgrounds": ["lifelong_resident", "recent_migrant", "returning_native"],
        "challenges": [
            "property_damage",
            "job_uncertainty",
            "community_displacement",
            "cultural_loss",
        ],
        "adaptations": [
            "elevated_homes",
            "new_skills",
            "community_networks",
            "cultural_preservation",
        ],
    },
    "urban_worker": {
        "professions": [
            "office_worker",
            "delivery_driver",
            "healthcare_worker",
            "teacher",
            "service_worker",
        ],
        "ages": ["young_adult", "middle_aged"],
        "backgrounds": ["native", "immigrant", "student"],
        "challenges": [
            "commuting_difficulties",
            "energy_costs",
            "health_impacts",
            "economic_pressure",
        ],
        "adaptations": [
            "remote_work",
            "public_transport",
            "community_gardens",
            "energy_efficiency",
        ],
    },
    "rural_farmer": {
        "professions": [
            "crop_farmer",
            "livestock_farmer",
            "agricultural_worker",
            "small_business_owner",
        ],
        "ages": ["young_adult", "middle_aged", "elderly"],
        "backgrounds": ["family_farm", "new_farmer", "migrant_worker"],
        "challenges": [
            "crop_failure",
            "water_scarcity",
            "market_uncertainty",
            "land_degradation",
        ],
        "adaptations": [
            "drought_resistant_crops",
            "water_harvesting",
            "diversification",
            "cooperative_farming",
        ],
    },
}
