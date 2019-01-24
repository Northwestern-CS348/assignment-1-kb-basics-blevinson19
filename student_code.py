import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if isinstance(fact,Rule):
            print("Asserting rules not in scope of assignment 1!")
        elif isinstance(fact, Fact) and fact not in self.facts:
            self.facts.append(fact)
            print("Asserting {!r}".format(fact))

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        found_binding = False
        if isinstance(fact,Rule):
            print("Asking for rules is not in scope of assignment1!")
        elif isinstance(fact,Fact):
            lob = ListOfBindings()

            for f in self.facts:
                #DEBUG
                # if f.statement.predicate == fact.statement.predicate:
                #     print(f.statement)
                bindings = Bindings()
                if match(f.statement,fact.statement,bindings) != False:
                    lob.add_bindings(bindings,fact)
                    found_binding = True
        if found_binding == True:
            return lob
        else:
            return False
