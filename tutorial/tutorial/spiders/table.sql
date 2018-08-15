-- Table: public.scrapy_detik

-- DROP TABLE public.scrapy_detik;

CREATE TABLE public.scrapy_detik
(
    id text COLLATE pg_catalog."default" NOT NULL DEFAULT (uuid_generate_v4())::text,
    date text COLLATE pg_catalog."default",
    content text COLLATE pg_catalog."default",
    url text COLLATE pg_catalog."default",
    title text COLLATE pg_catalog."default",
    CONSTRAINT scrapy_detik_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.scrapy_detik
    OWNER to postgres;