CREATE TABLE IF NOT EXISTS contracts (
    customer_id TEXT,
    module TEXT,
    expiry_date TEXT,
    price REAL
);

INSERT INTO contracts VALUES
('A001', 'Analytics', '2025-12-31', 4999.0),
('B002', 'Reporting', '2026-06-30', 2999.0),
('C003', 'Compliance', '2025-09-15', 3999.0),
('D004', 'DataHub', '2026-03-01', 5999.0);
