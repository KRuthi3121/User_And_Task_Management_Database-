# User & Task Management – MongoDB

## Overview
A Python + MongoDB project demonstrating schema design, CRUD operations, indexing, aggregation pipelines, and atomic updates.

## Data Model
- **Users**: user_id, name, email, created_at
- **Tasks**: task_id, title, status, priority, user_id, created_at

**Design choice:** Tasks reference users by `user_id`. Tasks are unbounded and frequently updated. Referencing avoids document growth and supports efficient updates and indexed queries.

## Indexes
- `tasks.user_id` → fast task lookup per user
- `tasks.user_id + tasks.created_at` → efficient sorting for recent tasks

Indexes are created at startup.

## CRUD
- Create users and tasks
- Fetch tasks by user
- Atomic update of status and priority
- Safe delete of tasks

## Aggregation
- Count tasks per status for a user
- Fetch most recent tasks

## Concurrency & Safety
MongoDB guarantees document-level atomicity. Updates use `update_one` with `$set`, preventing partial writes.

## Atomicity Guarantee
All task updates use single-document `update_one` operations. MongoDB guarantees atomicity at the document level, ensuring no partial or inconsistent writes during concurrent updates.

## Execution
1. Start MongoDB:
   ```bash
   mongod