"""
Climate Futures Storyteller - AI Agent for generating climate change narratives.

This module contains the main ClimateStoryteller class that generates compelling,
realistic stories about how climate change is transforming daily life around the world.
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

from regional_data import (
    CHARACTER_TEMPLATES,
    CLIMATE_IMPACT_DESCRIPTIONS,
    REGIONAL_CLIMATE_DATA,
)


class ClimateStoryteller:
    """
    AI storyteller specializing in climate change narratives.

    Creates compelling, realistic stories that highlight how climate change is
    transforming daily life around the world, set between present day and 2050.
    """

    def __init__(self):
        """Initialize the Climate Storyteller with regional data and templates."""
        self.regional_data = REGIONAL_CLIMATE_DATA
        self.impact_descriptions = CLIMATE_IMPACT_DESCRIPTIONS
        self.character_templates = CHARACTER_TEMPLATES

        # Climate science base as of October 2025
        self.climate_facts = {
            "global_temperature": "1.5°C above pre-industrial levels",
            "extreme_weather": "increasing frequency of floods, droughts, heatwaves, wildfires",
            "sea_level_rise": "accelerating with regional variations",
            "agricultural_zones": "shifting poleward and upward",
            "biodiversity": "accelerating loss and ecosystem disruption",
        }

    def generate_story(
        self,
        location: str = None,
        climate_impact: str = None,
        character_focus: str = None,
        story_length: int = 1200,
    ) -> str:
        """
        Generate a climate futures story.

        Args:
            location: Specific location (e.g., "Miami, Florida", "Bangladesh Delta")
            climate_impact: Type of climate impact (e.g., "sea_level_rise", "drought")
            character_focus: Character type focus (e.g., "coastal_community", "urban_worker")
            story_length: Target word count (default 1200)

        Returns:
            Generated story as a string
        """
        # Select random parameters if not specified
        if not location:
            location = self._select_random_location()
        if not climate_impact:
            climate_impact = self._select_random_climate_impact()
        if not character_focus:
            character_focus = self._select_random_character_focus()

        # Get regional data for the location
        region_data = self._get_region_data(location, climate_impact)

        # Create character profile
        character = self._create_character(character_focus, region_data)

        # Generate story structure
        story_parts = self._generate_story_structure(
            character, region_data, climate_impact
        )

        # Write the complete story
        story = self._write_story(story_parts, character, region_data, story_length)

        return story

    def _select_random_location(self) -> str:
        """Select a random location from available regional data."""
        all_locations = []
        for region_type, locations in self.regional_data.items():
            all_locations.extend(locations.keys())
        return random.choice(all_locations)

    def _select_random_climate_impact(self) -> str:
        """Select a random climate impact type."""
        impacts = list(self.impact_descriptions.keys())
        return random.choice(impacts)

    def _select_random_character_focus(self) -> str:
        """Select a random character focus type."""
        return random.choice(list(self.character_templates.keys()))

    def _get_region_data(self, location: str, climate_impact: str) -> Dict:
        """Get regional data for the specified location and climate impact."""
        # Find the region that contains this location
        for region_type, locations in self.regional_data.items():
            if location in locations:
                region_data = locations[location].copy()
                region_data["region_type"] = region_type
                region_data["location"] = location
                return region_data

        # Fallback to generic data if location not found
        return {
            "region_type": "generic",
            "location": location,
            "climate_impacts": [climate_impact],
            "specific_details": {},
            "cultural_context": "Diverse community adapting to climate change",
        }

    def _create_character(self, character_focus: str, region_data: Dict) -> Dict:
        """Create a detailed character profile."""
        template = self.character_templates[character_focus]

        character = {
            "name": self._generate_name(),
            "age_group": random.choice(template["ages"]),
            "profession": random.choice(template["professions"]),
            "background": random.choice(template["backgrounds"]),
            "location": region_data["location"],
            "challenges": random.sample(
                template["challenges"], k=min(2, len(template["challenges"]))
            ),
            "adaptations": random.sample(
                template["adaptations"], k=min(2, len(template["adaptations"]))
            ),
            "personal_story": self._generate_personal_background(
                character_focus, region_data
            ),
        }

        return character

    def _generate_name(self) -> str:
        """Generate a culturally appropriate name."""
        names = [
            "Maria",
            "Ahmed",
            "Sarah",
            "Chen",
            "Fatima",
            "James",
            "Priya",
            "Diego",
            "Aisha",
            "Michael",
            "Yuki",
            "Carlos",
            "Nadia",
            "David",
            "Lakshmi",
            "Hassan",
        ]
        return random.choice(names)

    def _generate_personal_background(
        self, character_focus: str, region_data: Dict
    ) -> str:
        """Generate a personal background for the character."""
        backgrounds = {
            "coastal_community": [
                "grew up by the water, learned to fish from grandparents",
                "moved here for work, fell in love with the ocean",
                "family has lived here for generations, watching the tides change",
            ],
            "urban_worker": [
                "came to the city for opportunities, now navigating new challenges",
                "born and raised in the neighborhood, seeing it transform",
                "moved here recently, learning to adapt to urban climate impacts",
            ],
            "rural_farmer": [
                "inherited the family farm, learning new ways to work the land",
                "started farming after a career change, embracing sustainable practices",
                "grew up in the countryside, now teaching others about adaptation",
            ],
            "pregnant_woman": [
                "discovered she was pregnant just as the climate impacts became more severe",
                "had her first child during a drought, now expecting her second during floods",
                "moved to the city for better healthcare, but climate change is making access difficult",
            ],
            "new_mother": [
                "gave birth during the worst heatwave in years, now caring for her newborn",
                "had her baby during flooding season, learning to navigate motherhood in crisis",
                "became a mother in a time of climate uncertainty, adapting daily to new challenges",
            ],
            "healthcare_worker": [
                "trained as a community health worker to serve her community during climate crises",
                "became a midwife to help women give birth safely despite climate challenges",
                "works as a nurse, seeing firsthand how climate change affects maternal health",
            ],
        }

        return random.choice(
            backgrounds.get(character_focus, ["adapting to changing times"])
        )

    def _get_pregnancy_stage(self, character: Dict) -> str:
        """Get pregnancy stage description for maternal health stories."""
        stages = [
            "in her first trimester",
            "in her second trimester",
            "in her third trimester",
            "expecting her first child",
            "carrying her second child",
            "pregnant with twins",
        ]
        return random.choice(stages)

    def _generate_story_structure(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> Dict:
        """Generate the structure and key elements of the story."""
        # Set story timeframe (present to 2050)
        story_year = random.randint(2025, 2050)

        # Create before/after comparison
        before_year = story_year - random.randint(5, 15)

        story_structure = {
            "title": self._generate_title(character, region_data, climate_impact),
            "year": story_year,
            "before_year": before_year,
            "opening_scene": self._create_opening_scene(
                character, region_data, climate_impact
            ),
            "before_scene": self._create_before_scene(
                character, region_data, before_year
            ),
            "transition": self._create_transition(
                character, region_data, climate_impact
            ),
            "present_challenges": self._create_present_challenges(
                character, region_data, climate_impact
            ),
            "adaptations": self._create_adaptations(
                character, region_data, climate_impact
            ),
            "community_response": self._create_community_response(
                character, region_data, climate_impact
            ),
            "reflection": self._create_reflection(
                character, region_data, climate_impact
            ),
            "sensory_details": self._get_sensory_details(climate_impact),
            "daily_changes": self._get_daily_changes(climate_impact),
        }

        return story_structure

    def _generate_title(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Generate a compelling story title."""
        titles = {
            "sea_level_rise": [
                "The New Shoreline",
                "When the Water Came",
                "Rising Tides, Rising Hope",
                "The Last Beach House",
            ],
            "drought": [
                "The Thirsty Season",
                "When the Rains Stopped",
                "Learning to Live with Less",
                "The Water Keepers",
            ],
            "extreme_heat": [
                "The Long Summer",
                "When the Air Burned",
                "Finding Shade",
                "The Cool Places",
            ],
            "wildfire": [
                "The Orange Sky",
                "When the Mountains Burned",
                "Learning to Live with Fire",
                "The Fire Keepers",
            ],
            "flooding_events": [
                "When the Roads Disappeared",
                "The Water Between Us",
                "Flooded Paths, Open Hearts",
                "Rising Waters, Rising Hope",
            ],
            "vector_borne_diseases": [
                "The Buzz of Danger",
                "When Mosquitoes Multiply",
                "Protecting Two Lives",
                "The Invisible Threat",
            ],
        }

        # Special titles for maternal health stories
        if character.get("profession") in ["pregnant_woman", "new_mother"]:
            maternal_titles = {
                "flooding_events": [
                    "The Road to the Clinic",
                    "When Water Blocks the Way",
                    "Flooded Paths, Mother's Heart",
                    "The Journey Through Water",
                ],
                "extreme_heat": [
                    "The Heat of New Life",
                    "When the Sun Burns Too Bright",
                    "Cooling the Fire Within",
                    "The Longest Summer",
                ],
                "vector_borne_diseases": [
                    "The Buzz of Fear",
                    "Protecting Two Hearts",
                    "When Mosquitoes Threaten Life",
                    "The Invisible Enemy",
                ],
            }
            if climate_impact in maternal_titles:
                return random.choice(maternal_titles[climate_impact])

        return random.choice(titles.get(climate_impact, ["Adapting to Change"]))

    def _create_opening_scene(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Create the opening scene of the story."""
        opening_templates = {
            "sea_level_rise": f"I never thought I'd need a boat to get to my own front door. But here I am, {character['name']}, paddling through what used to be my neighborhood street, past the old oak tree that now stands knee-deep in brackish water.",
            "drought": f"The sound of water is different now. {character['name']} remembers when the river used to rush past their window, but today it's just a trickle, and the silence is deafening.",
            "extreme_heat": f"At 6 AM, the air already feels like a warm blanket. {character['name']} steps outside and immediately feels the weight of the day ahead, knowing that by noon, the streets will be empty and the city will retreat indoors.",
            "wildfire": f"The sky is orange again today. {character['name']} has learned to read the color of the horizon like a weather forecast, and this particular shade means another day of staying inside, windows closed against the smoke.",
            "flooding_events": f"The rain started three days ago, and now {character['name']} watches the water rise around their home, knowing that today's antenatal appointment might be impossible to reach.",
            "vector_borne_diseases": f"The mosquitoes are worse this year, and {character['name']} feels their constant buzz as a threat to the life growing inside her, knowing that malaria during pregnancy can be devastating.",
        }

        # Special opening for maternal health scenarios
        if character.get("profession") in [
            "pregnant_woman",
            "new_mother",
        ] and climate_impact in [
            "flooding_events",
            "extreme_heat",
            "vector_borne_diseases",
        ]:
            if climate_impact == "flooding_events":
                return f"The water has cut off the road to the clinic again. {character['name']}, {self._get_pregnancy_stage(character)}, feels her baby kick as she watches the floodwaters rise, wondering how she'll make it to her antenatal appointment."
            elif climate_impact == "extreme_heat":
                return f"The heat is unbearable today, and {character['name']} feels her body struggling under the weight of both pregnancy and the scorching sun, knowing that heat stress can be dangerous for her unborn child."
            elif climate_impact == "vector_borne_diseases":
                return f"The mosquitoes are relentless this season, and {character['name']} feels their constant presence as a threat to her pregnancy, knowing that malaria can cause complications for both her and her baby."

        return opening_templates.get(
            climate_impact, f"{character['name']} wakes up to another day of change."
        )

    def _create_before_scene(
        self, character: Dict, region_data: Dict, before_year: int
    ) -> str:
        """Create a scene showing life before climate impacts became severe."""
        return f"Back in {before_year}, things were different. {character['name']} remembers when {self._get_before_memory(character, region_data)}. The rhythm of daily life was predictable, comfortable, taken for granted."

    def _get_before_memory(self, character: Dict, region_data: Dict) -> str:
        """Generate a specific memory from before climate impacts."""
        memories = {
            "coastal_community": [
                "the morning jog along the beach was a daily ritual",
                "the sound of waves was the soundtrack to every evening",
                "fishing trips were about adventure, not necessity",
                "the community gathered on the pier every sunset",
            ],
            "urban_worker": [
                "the subway was crowded but reliable",
                "summer meant outdoor festivals and street fairs",
                "the city's energy was infectious and constant",
                "weekend walks through the park were restorative",
            ],
            "rural_farmer": [
                "the seasons followed a predictable pattern",
                "the sound of rain on the roof was music",
                "the harvest was a time of celebration and abundance",
                "the land provided everything the community needed",
            ],
        }

        return random.choice(
            memories.get(
                character.get("profession", "coastal_community"), ["life was simpler"]
            )
        )

    def _create_transition(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Create the transition showing how things began to change."""
        return f"But change came gradually, then suddenly. {character['name']} noticed the small things first - {self._get_early_signs(climate_impact)}. Then the big changes started happening faster than anyone expected."

    def _get_early_signs(self, climate_impact: str) -> str:
        """Get early signs of climate impact."""
        signs = {
            "sea_level_rise": "the high tides reaching further up the beach, the storm drains backing up more often",
            "drought": "the wells running dry earlier each year, the crops needing more water than before",
            "extreme_heat": "the summer days getting longer and hotter, the nights offering less relief",
            "wildfire": "the fire season starting earlier each year, the smoke becoming a regular visitor",
        }
        return signs.get(climate_impact, "the small changes that added up")

    def _create_present_challenges(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Create a scene showing current challenges."""
        return f"Now, in {region_data.get('year', 2030)}, {character['name']} faces new realities every day. {self._get_present_challenge_description(character, region_data, climate_impact)}"

    def _get_present_challenge_description(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Get description of present challenges."""
        challenges = {
            "sea_level_rise": f"The water has claimed {character['name']}'s favorite walking path, and the insurance company won't cover the flood damage anymore. Every storm brings new anxiety about what might be lost next.",
            "drought": f"{character['name']} has learned to measure water in drops, not gallons. The garden that once fed the family now struggles to survive, and the community well runs dry by mid-summer.",
            "extreme_heat": f"The heat has reshaped {character['name']}'s entire day. Work starts at dawn and ends by noon, and the afternoons are spent in whatever cool place can be found.",
            "wildfire": f"Every summer, {character['name']} keeps a bag packed by the door. The evacuation orders come with little warning, and the smoke makes it hard to breathe even when the flames are miles away.",
            "flooding_events": f"The roads to the clinic are impassable again, and {character['name']} worries about missing critical antenatal appointments. The floodwaters have cut off access to healthcare when it's needed most.",
            "vector_borne_diseases": f"The mosquitoes are relentless this season, and {character['name']} feels their constant presence as a threat to her pregnancy, knowing that malaria can cause complications for both her and her baby.",
        }

        # Special challenges for maternal health scenarios
        if character.get("profession") in ["pregnant_woman", "new_mother"]:
            maternal_challenges = {
                "flooding_events": f"The floodwaters have cut off the road to the clinic, and {character['name']}, {self._get_pregnancy_stage(character)}, worries about missing her antenatal appointment. She can feel her baby kick as she watches the water rise, wondering how she'll get the care she needs.",
                "extreme_heat": f"The heat is unbearable, and {character['name']} feels her body struggling under the weight of both pregnancy and the scorching sun. She knows heat stress can be dangerous for her unborn child, but she must continue working to support her family.",
                "vector_borne_diseases": f"The mosquitoes are worse this year, and {character['name']} feels their constant buzz as a threat to the life growing inside her. She knows malaria during pregnancy can cause premature birth, low birth weight, or even death for her baby.",
            }
            if climate_impact in maternal_challenges:
                return maternal_challenges[climate_impact]

        return challenges.get(
            climate_impact, f"{character['name']} faces new challenges every day."
        )

    def _create_adaptations(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Create a scene showing how the character has adapted."""
        return f"But {character['name']} has learned to adapt. {self._get_adaptation_description(character, region_data, climate_impact)}"

    def _get_adaptation_description(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Get description of adaptations."""
        adaptations = {
            "sea_level_rise": f"The house now sits on stilts, and {character['name']} has learned to navigate the neighborhood by boat. The community has built floating gardens and installed pumps that run on solar power.",
            "drought": f"{character['name']} has become a master of water conservation, collecting every drop of rainwater and growing drought-resistant crops. The community shares resources and knowledge about sustainable farming.",
            "extreme_heat": f"The home has been retrofitted with better insulation and cooling systems that run on renewable energy. {character['name']} has learned to work with the heat, not against it.",
            "wildfire": f"The property has been cleared of flammable materials, and {character['name']} has learned to read the wind and weather patterns. The community has established early warning systems and evacuation plans.",
            "flooding_events": f"The community has established emergency transport systems and mobile clinics that can reach flooded areas. {character['name']} has learned to identify safe routes and alternative healthcare options when the main roads are impassable.",
            "vector_borne_diseases": f"The community has implemented comprehensive mosquito control measures and distributed insecticide-treated nets. {character['name']} has learned to protect herself and her family through proper net usage and environmental management.",
        }

        # Special adaptations for maternal health scenarios
        if character.get("profession") in ["pregnant_woman", "new_mother"]:
            maternal_adaptations = {
                "flooding_events": f"The community has established emergency transport systems and mobile clinics that can reach flooded areas. {character['name']} has learned to identify safe routes and alternative healthcare options when the main roads are impassable. Community health workers now make home visits during floods to ensure pregnant women receive the care they need.",
                "extreme_heat": f"The community has set up cooling centers and shade structures where pregnant women can rest during the hottest parts of the day. {character['name']} has learned to adjust her work schedule and stay hydrated, while community health workers provide regular check-ups to monitor her and her baby's health.",
                "vector_borne_diseases": f"The community has implemented comprehensive mosquito control measures and distributed insecticide-treated nets. {character['name']} has learned to protect herself and her unborn child through proper net usage, environmental management, and regular malaria prevention medication. Community health workers provide education and support to ensure safe pregnancies.",
            }
            if climate_impact in maternal_adaptations:
                return maternal_adaptations[climate_impact]

        return adaptations.get(
            climate_impact, f"{character['name']} has found new ways to thrive."
        )

    def _create_community_response(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Create a scene showing community response and solidarity."""
        return f"The community has come together in ways {character['name']} never expected. {self._get_community_response_description(character, region_data, climate_impact)}"

    def _get_community_response_description(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Get description of community response."""
        responses = {
            "sea_level_rise": "Neighbors help each other with flood preparations, share boats for transportation, and work together to maintain the community's resilience.",
            "drought": "The community has established water-sharing agreements, created community gardens, and organized workshops on sustainable living.",
            "extreme_heat": "Cooling centers have been set up in community buildings, and neighbors check on each other during heat waves, especially the elderly and vulnerable.",
            "wildfire": "The community has formed fire watch groups, established evacuation protocols, and created support networks for those who have lost homes.",
        }
        return responses.get(
            climate_impact, "The community has found strength in working together."
        )

    def _create_reflection(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Create a reflective ending to the story."""
        return f"As {character['name']} looks out at the changed landscape, there's a mix of loss and hope. The world is different now, but the human spirit of adaptation and community resilience shines through. {self._get_hopeful_ending(character, region_data, climate_impact)}"

    def _get_hopeful_ending(
        self, character: Dict, region_data: Dict, climate_impact: str
    ) -> str:
        """Get a hopeful ending for the story."""
        endings = {
            "sea_level_rise": "The water may have claimed some land, but it has also brought the community closer together, creating new ways of living that are more connected to the natural world.",
            "drought": "The scarcity of water has taught the community to value every resource, creating a more sustainable way of life that honors the land and each other.",
            "extreme_heat": "The heat has forced innovation and adaptation, leading to new technologies and community practices that are more resilient and sustainable.",
            "wildfire": "The fires have taught the community to respect the power of nature while building stronger bonds and more resilient communities.",
        }
        return endings.get(
            climate_impact,
            "The challenges have brought out the best in people, creating new possibilities for the future.",
        )

    def _get_sensory_details(self, climate_impact: str) -> str:
        """Get sensory details for the climate impact."""
        return self.impact_descriptions.get(climate_impact, {}).get(
            "sensory_details", "The world feels different now."
        )

    def _get_daily_changes(self, climate_impact: str) -> str:
        """Get description of daily changes due to climate impact."""
        return self.impact_descriptions.get(climate_impact, {}).get(
            "daily_changes", "Daily life has changed in ways both small and large."
        )

    def _write_story(
        self, story_parts: Dict, character: Dict, region_data: Dict, target_length: int
    ) -> str:
        """Write the complete story from the story parts."""
        story = f"# {story_parts['title']}\n\n"
        story += f"*A climate futures story set in {region_data['location']}, {story_parts['year']}*\n\n"

        # Opening scene
        story += f"{story_parts['opening_scene']}\n\n"

        # Before scene
        story += f"{story_parts['before_scene']}\n\n"

        # Transition
        story += f"{story_parts['transition']}\n\n"

        # Present challenges
        story += f"{story_parts['present_challenges']}\n\n"

        # Adaptations
        story += f"{story_parts['adaptations']}\n\n"

        # Community response
        story += f"{story_parts['community_response']}\n\n"

        # Reflection
        story += f"{story_parts['reflection']}\n\n"

        # Add sensory details and daily changes throughout
        story += (
            f"The sensory details are everywhere: {story_parts['sensory_details']}\n\n"
        )
        story += f"Daily life has transformed: {story_parts['daily_changes']}\n\n"

        # Add character's personal story
        story += f"For {character['name']}, this journey has been deeply personal. {character['personal_story']}, and now {character['name']} is part of a community learning to thrive in a changing world.\n\n"

        # Add regional context
        if "cultural_context" in region_data:
            story += f"The cultural context of {region_data['location']} adds another layer to this story. {region_data['cultural_context']}, and this heritage provides both challenges and strengths as the community adapts to new realities.\n\n"

        # Add climate science context
        story += f"This story reflects the reality of climate change as we understand it in 2025: {self.climate_facts['global_temperature']}, with {self.climate_facts['extreme_weather']}, and {self.climate_facts['sea_level_rise']}. The impacts are real, but so is the human capacity for adaptation and resilience.\n\n"

        story += f"*This story is part of the Climate Futures Storyteller project, creating narratives that help us understand and connect with the human experience of climate change.*"

        return story

    def list_available_locations(self) -> List[str]:
        """List all available locations for story generation."""
        locations = []
        for region_type, locations_dict in self.regional_data.items():
            locations.extend(locations_dict.keys())
        return locations

    def list_available_impacts(self) -> List[str]:
        """List all available climate impacts for story generation."""
        return list(self.impact_descriptions.keys())

    def list_available_characters(self) -> List[str]:
        """List all available character types for story generation."""
        return list(self.character_templates.keys())


# Example usage and testing
if __name__ == "__main__":
    # Initialize the storyteller
    storyteller = ClimateStoryteller()

    # Generate a sample story
    print("Generating a sample climate futures story...")
    story = storyteller.generate_story(
        location="miami_florida",
        climate_impact="sea_level_rise",
        character_focus="coastal_community",
    )

    print(story)
    print("\n" + "=" * 50)
    print("Available locations:", storyteller.list_available_locations())
    print("Available impacts:", storyteller.list_available_impacts())
    print("Available characters:", storyteller.list_available_characters())
