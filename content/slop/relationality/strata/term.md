---
title: Term
aliases:
  - "Term"
  - "term"
date-created: 2026-02-28T00:00:00---
# Term Stratum

Term-level acts introduce variables, binders, fixpoint constructors, and the
evaluation contexts that carry syntax forward.  This stratum is where the trace
machinery hardens into the objects manipulated by the judgement layer.

Acts classified under **term** grouped by phase.

## Free Phase

| Act | Title |
| --- | --- |
| `EquateEventually` | [Equating Eventually](equate-eventually.md) |
| `RecognizeEquateEventually` | [Recognizing Eventual Equivalence](recognize-equate-eventually.md) |
| `EnforceEquateEventuallyLaw` | [Enforcing Eventual Equivalence Law](enforce-equate-eventually-law.md) |
| `SeedTerm` | [Seeding Terms](seed-term.md) |
| `BindTerm` | [Binding Terms](bind-term.md) |
| `PresentVariableTerm` | [Presenting Variable Term](present-variable-term.md) |
| `FormTermBody` | [Forming Term Body](form-term-body.md) |
| `FormFunctionTerm` | [Forming Function Term](form-function-term.md) |
| `PairApplication` | [Pairing Application](pair-application.md) |
| `FormApplicationTerm` | [Forming Application Term](form-application-term.md) |
| `PairLeastFix` | [Pairing Least Fix](pair-least-fix.md) |
| `FormLeastFixTerm` | [Forming Least Fix Term](form-least-fix-term.md) |
| `PairGreatestFix` | [Pairing Greatest Fix](pair-greatest-fix.md) |
| `FormGreatestFixTerm` | [Forming Greatest Fix Term](form-greatest-fix-term.md) |
| `TypeSeed` | [Seeding Types](type-seed.md) |
| `TypeVariable` | [Typing Variables](type-variable.md) |
| `TypeApplication` | [Typing Applications](type-application.md) |
| `WeakeningSeed` | [Seeding Weakening](weakening-seed.md) |
| `GreatestFixpointTypeSeed` | [Seeding Greatest Fixpoint Typing](greatest-fixpoint-type-seed.md) |
| `GreatestFixpointTypingStep` | [Stepping Greatest Fixpoint Typing](greatest-fixpoint-typing-step.md) |
| `BinderSeed` | [Seeding Binder](binder-seed.md) |
| `BinderTransport` | [Transporting Binder](binder-transport.md) |
| `BinderApplication` | [Applying Binder](binder-application.md) |
| `SubstitutionTerm` | [Forming Substitution Term](substitution-term.md) |
| `Reduce` | [Reducing](reduce.md) |
| `StepTrace` | [Tracing Steps](step-trace.md) |
| `Normalization` | [Normalizing](normalization.md) |
| `EquateContexts` | [Equating Contexts](equate-contexts.md) |
| `SeedEvaluationContext` | [Seeding Evaluation Context](seed-evaluation-context.md) |
| `BuildEvaluationContext` | [Building Evaluation Context](build-evaluation-context.md) |
| `SeedValue` | [Seeding Values](seed-value.md) |
| `RecognizeValue` | [Recognizing Values](recognize-value.md) |
