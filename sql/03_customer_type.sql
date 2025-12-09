SELECT CustomerID,
       CASE WHEN MIN(InvoiceDate) = MAX(InvoiceDate)
            THEN 'New' ELSE 'Returning' END AS CustomerType
FROM OnlineRetail
GROUP BY CustomerID;
