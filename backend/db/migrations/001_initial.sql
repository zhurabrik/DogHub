CREATE TABLE IF NOT EXISTS templates (
  id SERIAL PRIMARY KEY,
  meta JSONB NOT NULL
);

INSERT INTO templates (meta) values
('{
  "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Stadtbild_M%C3%BCnchen.jpg/2560px-Stadtbild_M%C3%BCnchen.jpg",
  "description": "just a picture",
  "title": "just a picture",
  "address": "some address"
}'),
('{
  "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bratskfountain.jpg/300px-Bratskfountain.jpg",
  "description": "just a picture of Bratsk",
  "title": "just a picture of Bratsk",
  "address": "some address"
}')
ON CONFLICT (id) DO NOTHING;