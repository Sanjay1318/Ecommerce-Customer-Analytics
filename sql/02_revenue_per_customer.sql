SELECT CustomerID,
       SUM(Quantity * UnitPrice) AS TotalRevenue
FROM OnlineRetail
GROUP BY CustomerID
ORDER BY TotalRevenue DESC;
