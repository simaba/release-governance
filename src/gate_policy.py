"""Operational gate policy for risk-tiered AI release decisions."""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from risk_scoring import RiskInputs, RiskTier, score_risk


class ReleaseDecision(str, Enum):
    GO = "go"
    CONDITIONAL_GO = "conditional_go"
    NO_GO = "no_go"


GATE_LABELS = {
    "domain_and_data_coverage": "G1. Domain and data coverage",
    "uncertainty_handling": "G2. Uncertainty handling",
    "fallback_and_degraded_mode": "G3. Fallback and degraded mode",
    "monitoring_and_observability": "G4. Monitoring and observability",
    "human_escalation_and_override": "G5. Human escalation and override",
    "incident_response_and_recovery": "G6. Incident response and recovery",
    "accountability_signoff": "G7. Accountability sign-off",
    "post_release_review_plan": "G8. Post-release review plan",
}


REQUIRED_GATES = {
    RiskTier.LOW: [
        "domain_and_data_coverage",
        "uncertainty_handling",
        "monitoring_and_observability",
    ],
    RiskTier.MEDIUM: [
        "domain_and_data_coverage",
        "uncertainty_handling",
        "fallback_and_degraded_mode",
        "monitoring_and_observability",
        "human_escalation_and_override",
        "post_release_review_plan",
    ],
    RiskTier.HIGH: [
        "domain_and_data_coverage",
        "uncertainty_handling",
        "fallback_and_degraded_mode",
        "monitoring_and_observability",
        "human_escalation_and_override",
        "incident_response_and_recovery",
        "accountability_signoff",
        "post_release_review_plan",
    ],
}


CRITICAL_GATES = {
    RiskTier.LOW: ["monitoring_and_observability"],
    RiskTier.MEDIUM: [
        "fallback_and_degraded_mode",
        "monitoring_and_observability",
        "human_escalation_and_override",
    ],
    RiskTier.HIGH: [
        "fallback_and_degraded_mode",
        "monitoring_and_observability",
        "incident_response_and_recovery",
        "accountability_signoff",
    ],
}


@dataclass
class ReleaseAssessment:
    score: int
    tier: RiskTier
    decision: ReleaseDecision
    required_gates: List[str]
    satisfied_gates: List[str]
    missing_gates: List[str]
    rationale: List[str]


def assess_release(risk_inputs: RiskInputs, evidence: Dict[str, bool]) -> ReleaseAssessment:
    score, tier = score_risk(risk_inputs)
    required_gates = REQUIRED_GATES[tier]
    satisfied_gates = [gate for gate in required_gates if evidence.get(gate, False)]
    missing_gates = [gate for gate in required_gates if not evidence.get(gate, False)]

    rationale: List[str] = []

    if not missing_gates:
        decision = ReleaseDecision.GO
        rationale.append("All required gates for the assessed risk tier are satisfied.")
    else:
        critical_missing = [gate for gate in CRITICAL_GATES[tier] if gate in missing_gates]
        if critical_missing:
            decision = ReleaseDecision.NO_GO
            rationale.append("One or more critical control gates are missing.")
        else:
            decision = ReleaseDecision.CONDITIONAL_GO
            rationale.append("Required gates are incomplete, but no critical gate is missing.")
            rationale.append("A conditional release should include owner, deadline, and compensating controls.")

    if tier == RiskTier.HIGH:
        rationale.append("High-risk releases require explicit accountability and incident response readiness.")
    elif tier == RiskTier.MEDIUM:
        rationale.append("Medium-risk releases should use phased rollout and tighter monitoring discipline.")
    else:
        rationale.append("Low-risk releases should still preserve rollback and basic observability.")

    return ReleaseAssessment(
        score=score,
        tier=tier,
        decision=decision,
        required_gates=required_gates,
        satisfied_gates=satisfied_gates,
        missing_gates=missing_gates,
        rationale=rationale,
    )


def build_risk_inputs(data: Dict[str, int]) -> RiskInputs:
    return RiskInputs(
        safety_impact=data["safety_impact"],
        regulatory_exposure=data["regulatory_exposure"],
        uncertainty_sensitivity=data["uncertainty_sensitivity"],
        operational_complexity=data["operational_complexity"],
        observability_maturity=data["observability_maturity"],
        fallback_readiness=data["fallback_readiness"],
    )
