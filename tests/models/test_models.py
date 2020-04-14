from tests.fixtures.models import DummyModel
from mesa_behaviors.history.binary import BinaryHistory
from tests.fixtures.agents import DummyAgent
from mesa_behaviors.utility.binary import BinaryMajorityUtility, BinaryMinorityUtility
from mesa_behaviors.strategies.binary_strategy import generate_binary_strategies
from mesa_behaviors.agents.population import generate_population, AgentLabels

from bitarray import bitarray

import random
from mesa.time import RandomActivation


def dummy_distribution(agent_labels: AgentLabels, size: int) -> AgentLabels:
    dumm = random.choices(["schadenfreuder", "normal"], [0.50, 0.50], k=size)
    return dumm


def test_model_integration():
    initial_history = bitarray([0, 0, 1])

    history = BinaryHistory(initial_history)

    typesMap = {
        "schadenfreuder": lambda: DummyAgent(
            generate_binary_strategies(4, 3),
            BinaryMinorityUtility(),
            history.retrieve,
            "personA",
        ),
        "normal": lambda: DummyAgent(
            generate_binary_strategies(4, 3),
            BinaryMajorityUtility(),
            history.retrieve,
            "personB",
        ),
    }
    generator = generate_population(dummy_distribution, typesMap, 100)
    agent_population = generator()
    model_terminal_steps = 20
    model = DummyModel(
        agent_population, RandomActivation, history, model_terminal_steps
    )

    while model.running is True:
        model.step()

        # assert history grows correctly
    assert len(model.history.retrieve()) == model_terminal_steps + 3

    # assert number of agents model has
    assert len(model.agents) == 100
