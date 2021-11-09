import torch
from switch_activation import SwitchActivation

import unittest

C1 = 0.7310585975646973
C2 = 0.2689414322376251

class SwitchActivationTest(unittest.TestCase):
    def test_simple_usage(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        relu_x = torch.relu(x).tolist()
        act = SwitchActivation(['relu'])

        act.train(False)
        self.assertEqual(act(x).tolist(), relu_x)

        act.train()
        self.assertEqual(act(x).tolist(), relu_x)

    def test_simple_two_activations(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        relu_x = torch.relu(x)
        sigmoid_x = torch.sigmoid(x)

        act = SwitchActivation(['relu', 'sigmoid'])
        with torch.no_grad():
            act._logits[0] = 1.0

        act.train(False)
        self.assertEqual(act(x).tolist(), relu_x.tolist())

    def test_two_activations_soft(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        relu_x = torch.relu(x)
        sigmoid_x = torch.sigmoid(x)

        act = SwitchActivation(['relu', 'sigmoid'])
        with torch.no_grad():
            act._logits[0] = 1.0

        act.train()
        self.assertTrue(
            act(x).tolist(), (C1 * relu_x + C2 * sigmoid_x).tolist()
        )

    def test_probs(self):
        act = SwitchActivation(['relu', 'sigmoid'])
        with torch.no_grad():
            act._logits[0] = 1.0
        self.assertEqual(act.probs[0].item(), C1)
        self.assertEqual(act.probs[1].item(), C2)

    def test_gelu(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        act = SwitchActivation(['gelu'])
        act(x)

    def test_swish(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        act = SwitchActivation(['swish'])
        act(x)

    def test_identity(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        act = SwitchActivation(['identity'])
        self.assertEqual(act(x).tolist(), x.tolist())

    def test_one(self):
        x = torch.tensor([-1.0, 1.0, 0.0, 0.5, 1.5, -2.5])
        act = SwitchActivation(['one'])
        self.assertEqual(act(x).tolist(), [1, 1, 1, 1, 1,1])
