---
name: i-test-driven-development 
description: Implement test-driven development (TDD) for approved user stories, spike candidates, or other implementation-ready work. Use after f-user-story-technical-readiness when Codex must verify story, architecture, and technical-review lineage; prevent duplicates; show exact test descriptions and metadata in chat for approval before writing tests; create or update approved tests; verify publication; update the TDD test registry; classify unlinked tests as duplicates, similar existing scope, bugs, new requirement candidates, out of scope, not actionable, or needing human review; create intake reconciliation reports; or route unlinked, duplicate, diverged, or contributor-created tests.
---
# Test-Driven Development (TDD)

## Purpose
This skill implements test-driven development (TDD) for approved user stories, spike candidates, or other implementation-ready work. It ensures that tests are written before or alongside the implementation code, and that the code is developed to pass those tests. This approach helps to ensure that the code meets the specified requirements and behaves as expected.

## Inputs

## Outputs

## Core Workflow

1. Read inputs
2. Validate testing plan
3. Implement TDD

### Step 1. Read inputs

Read the approved user story, spike candidate, or other implementation-ready work and its associated architecture and technical review.

### Step 2. Validate testing plan

Create or update approved tests based on the requirements.

### Step 3. Implement TDD

Use two separate agents to implement TDD: one agent for writing tests and another for writing implementation code. The test-writing agent should create tests before or alongside the implementation code. 
  - Agent A: Writes tests based on the approved user story, spike candidate, or other implementation-ready work.
  - Agent B: Writes implementation code based on the approved user story, spike candidate, or

The strategy both agents follow is to ensure that tests are written first, and the implementation code is developed to pass those tests. This approach ensures that the code meets the specified requirements and behaves as expected. This strategy is also known as "ping-pong" TDD, where Agent A and Agent B work in tandem, with Agent A writing a test and Agent B writing the corresponding implementation code to pass that test.

In all moment the user will be able to see the progress of both agents and approve or request changes to the tests or implementation code as needed. The agents will also ensure that any new tests or code are properly documented and linked to the relevant user story, spike candidate, or other implementation-ready work.


