CREATE TABLE IF NOT EXISTS todo (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            item VARCHAR(255) NOT NULL
        );

INSERT INTO todo (item)
VALUES ('Learn SQL'),('Build a REST API'),('Write Unit Tests');

SELECT id, item
FROM todo
where id = '0bdc9862-e4e2-4a2a-b6be-635a69878aa0';

UPDATE todo
SET item = 'Learn Advanced SQL'
WHERE id = '2fc05e90-0810-4028-91a2-7efb4f4e40a0' ;
 
 DELETE FROM todo
 where id = '2fc05e90-0810-4028-91a2-7efb4f4e40a0';