CREATE TABLE IF NOT EXISTS templates (
  id SERIAL PRIMARY KEY,
  meta JSONB NOT NULL
);

INSERT INTO templates (id, meta) values
(1, '{"path": "some/path/to/image"}'),
(2, '{"path2": "some/path/to/image2"}')
ON CONFLICT (id) DO NOTHING;