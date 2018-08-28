-- Table: public.scr_raw_content

-- DROP TABLE public.scr_raw_content;

CREATE TABLE public.scr_raw_content
(
    id text COLLATE pg_catalog."default" NOT NULL DEFAULT (uuid_generate_v4())::text,
    date text COLLATE pg_catalog."default",
    content text COLLATE pg_catalog."default",
    url text COLLATE pg_catalog."default",
    title text COLLATE pg_catalog."default",
    ctime time without time zone,
    crawl_agent integer,
    CONSTRAINT scrapy_detik_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.scr_raw_content
    OWNER to postgres;