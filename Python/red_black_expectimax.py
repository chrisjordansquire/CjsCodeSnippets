# Expectimax of a simple game where there is a 2N card deck of N black
# and N red cards. After drawing a card the player has the choice to
# stop or draw again, as long as cards remain. When the player stops,
# the final score is the number of black cards minus the number of red
# cards.

class RedBlackExpectimaxTree:
    def __init__(self, numberOfCards):
        self.numberOfCards = numberOfCards
        self.root = {'cardsInDeck': (self.numberOfCards, self.numberOfCards),
                     'cardsDrawn': (0, 0),
                     'type': 'action'}

    def buildTree(self):
        nodesToProcess = [self.root]
        while nodesToProcess:
            node = nodesToProcess.pop()
            self._processNode(node, nodesToProcess)

    def _valueNode(self, node):
        if node['type'] == 'chance':
            numberOfBlackInDeck, numberOfRedInDeck = node['cardsInDeck']
            totalInDeck = numberOfBlackInDeck + numberOfRedInDeck
            drawBlackValue = 0
            drawRedValue = 0
            if numberOfBlackInDeck > 0:
                probabilityOfBlack = numberOfBlackInDeck / totalInDeck
                self._valueNode(node['drawBlack'])
                drawBlackValue = node['drawBlack']['value'] * probabilityOfBlack
            if numberOfRedInDeck > 0:
                probabilityOfRed = numberOfRedInDeck / totalInDeck
                self._valueNode(node['drawRed'])
                drawRedValue = node['drawRed']['value'] * probabilityOfRed
            return drawBlackValue + drawRedValue
        elif node['type'] == 'action':
            node['stopValue'] = node['stop']['value']
            if sum(node['cardsInDeck']) > 0:
                node['goValue'] = self._valueNode(node['go'])
                node['value'] = max(node['goValue'], node['stopValue'])
            else:
                node['value'] = node['stopValue']

    def valueTree(self):
        self._valueNode(self.root)

    def _processNode(self, node, nodesToProcess):
        if node['type'] == 'action':
            self._processActionNode(node, nodesToProcess)
        elif node['type'] == 'chance':
            self._processChanceNode(node, nodesToProcess)

    def _processActionNode(self, node, nodesToProcess):
        numberOfBlack, numberOfRed = node['cardsDrawn']
        cardsRemaining = sum(node['cardsInDeck'])
        if cardsRemaining > 0:
            chanceNode = node.copy()
            chanceNode['type'] = 'chance'
            node['go'] = chanceNode
            nodesToProcess.append(chanceNode)
        value = numberOfBlack - numberOfRed
        node['stop'] = {'type': 'terminal', 'value': value}

    def _processChanceNode(self, node, nodesToProcess):
        numberOfBlackInDeck, numberOfRedInDeck = node['cardsInDeck']
        numberOfBlackDrawn, numberOfRedDrawn = node['cardsDrawn']
        if numberOfBlackInDeck > 0:
            drawBlackNode = {'cardsInDeck': (numberOfBlackInDeck - 1, numberOfRedInDeck),
                             'cardsDrawn': (numberOfBlackDrawn + 1, numberOfRedDrawn),
                             'type': 'action'}
            nodesToProcess.append(drawBlackNode)
            node['drawBlack'] = drawBlackNode
        if numberOfRedInDeck > 0:
            drawRedNode = {'cardsInDeck': (numberOfBlackInDeck, numberOfRedInDeck - 1),
                           'cardsDrawn': (numberOfBlackDrawn, numberOfRedDrawn + 1),
                           'type': 'action'}
            node['drawRed'] = drawRedNode
            nodesToProcess.append(drawRedNode)
