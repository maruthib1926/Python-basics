# Bug Report

## Bug ID
BUG-001

## Bug Title
Empty Employee ID Validation Failure

## Module
Employee Validation

## Severity
Medium

## Priority
High

## Test Input
Employee ID: Empty

## Expected Result
Invalid employee ID

## Actual Result
Employee ID is accepted as valid.

## Status
**closed**

## Root Cause
Incorrect validation condition.

## Fix
Change employee_id == "0" to employee_id == "".
