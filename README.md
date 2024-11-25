# IS-Restaurant-Chain

## Deploy Web app

https://restaurant-chain-9nr7.onrender.com

## Overview

A restaurant chain operates on legacy POS systems, separate loyalty programs, and mobile apps, leading to overhead inefficiencies. Data is isolated across systems, limiting customer insights. Scaling requires replicating changes across systems, and adding new data/features requires complex coordination.

The fragmented systems limit the restaurant chain's ability to deliver seamless omnichannel experiences. For example, promotions and ordering are not integrated across POS, mobile apps, and loyalty programs, resulting in inconsistent messaging and experiences.

## Solution

The company needs cross-channel data sharing to enable personalized engagements, inventory coordination, and process optimization. The solution involves building microservices oriented around restaurant capabilities like ordering and loyalty programs. These would expose customer, sales, and menu data APIs managed by a gateway. This data is streamed to a cloud analytics platform for ML optimization. This approach incrementally decomposes monoliths over time into focused, decoupled services that deliver unified data access through standardized APIs.

### Specifications

- Develop microservices for ordering, loyalty, pricing, and promotions.
- Expose customer, menu, and sales data via APIs controlled by a gateway.
- Stream API data into a cloud analytics platform.
- Apply analytics and ML to optimize pricing and promotions.
