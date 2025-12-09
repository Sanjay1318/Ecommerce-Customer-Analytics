SELECT CustomerID, COUNT(InvoiceNo) AS TotalOrders
FROM OnlineRetail
GROUP BY CustomerID
ORDER BY TotalOrders DESC;
