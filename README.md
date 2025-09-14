# Price-Estimation-Model
This pipeline is designed to integrated seamlessly with a FastAPI + PostgreSQL setup to **dynamically update product prices** on the last day of each month, **based on price elasticity demand**.

**Core Logic**

For each product, the system:

- Calculates **price elasticity** based on historical order data from the database;
- Determines the new price based on elasticity:
  - If elasticity > -1 Price is increased by 2%
  - If elasticity < -1 Price is decreased by 2%
  - If elasticity = -1 Price is kept intact
