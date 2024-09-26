**Issue Summary**

*Duration:*  
The outage occurred on September 24, 2024, from 2:15 PM to 4:00 PM UTC, lasting approximately 1 hour and 45 minutes.

*Impact:*  
The issue caused significant delays in processing user requests on our e-commerce platform, with page load times increasing from the usual 1-2 seconds to over 30 seconds. Around 80% of users experienced these delays, leading to a drop in transaction rates and numerous complaints via customer support channels.

*Root Cause:*  
The root cause was an unanticipated surge in traffic coupled with a misconfigured database connection pool, which resulted in database connection exhaustion.

---

**Timeline**

- **2:15 PM:** Monitoring alert triggered due to a spike in the average page load time.
- **2:20 PM:** An engineer reviewed the alert and confirmed the issue by reproducing the slow page loads in the staging environment.
- **2:30 PM:** Initial assumption was high database load due to a long-running query. Query optimization was prioritized.
- **2:45 PM:** Query optimizations showed no improvement; database load metrics were within normal parameters.
- **3:00 PM:** Investigated application servers, suspecting high CPU/memory usage, but all metrics were normal.
- **3:10 PM:** Escalated to the Database and Infrastructure teams.
- **3:25 PM:** Noticed a rapid increase in the number of database connections in the connection pool.
- **3:30 PM:** Database team discovered that connection pool size had not been adjusted to handle peak loads.
- **3:35 PM:** A fix was proposed to increase the connection pool size.
- **3:45 PM:** Connection pool size was increased and application servers were restarted to apply changes.
- **3:50 PM:** Page load times began to return to normal.
- **4:00 PM:** Confirmed all services were stable, and the incident was marked as resolved.

---

**Root Cause and Resolution**

*Root Cause:*  
The sudden increase in traffic overwhelmed our database connection pool. Our connection pool was configured with a maximum of 100 connections, which was sufficient for normal traffic but insufficient for the unexpected surge. As a result, requests were queued waiting for an available connection, leading to significant delays. The monitoring alert misled us initially as it was configured to track database query performance but not connection pool saturation.

*Resolution:*  
After diagnosing the connection pool saturation, we increased the maximum pool size from 100 to 300 connections and adjusted the pool timeout settings. We then restarted the application servers to ensure the new settings were applied. This allowed the database to handle the increased number of concurrent connections, eliminating the bottleneck and reducing page load times to normal levels.

---

**Corrective and Preventative Measures**

*Improvements:*
1. **Monitoring Enhancements:** Add monitoring for database connection pool metrics, including the number of active connections and connection wait times.
2. **Scalability Testing:** Implement automated load testing during non-peak hours to simulate traffic surges and validate the application’s ability to handle them.
3. **Configuration Management:** Review and document configuration settings related to connection pools and other critical resources to ensure they align with expected traffic patterns.

*Tasks:*
1. **Add Connection Pool Monitoring:** Implement alerts for when the connection pool usage exceeds 80% for more than 5 minutes.
2. **Load Testing Integration:** Develop and automate load test scenarios in the CI/CD pipeline to simulate high traffic conditions.
3. **Configuration Audit:** Perform a full audit of database and application server configurations and update documentation to reflect current best practices.
4. **Capacity Planning:** Schedule regular reviews of traffic patterns and adjust resource allocations and configurations accordingly.
5. **Customer Communication Protocol:** Develop a standardized protocol for quickly informing customers of ongoing issues and expected resolution times.

These measures will help prevent future outages and improve our ability to respond to incidents quickly and effectively.
