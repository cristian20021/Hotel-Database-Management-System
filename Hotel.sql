PGDMP  "                    |            Hotel    16.1    16.0     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16466    Hotel    DATABASE     �   CREATE DATABASE "Hotel" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "Hotel";
                postgres    false            �            1259    16479    booking    TABLE     �   CREATE TABLE public.booking (
    bookingid integer NOT NULL,
    guestid integer,
    roomid integer,
    checkindate date,
    checkoutdate date,
    paymentstatus character varying(255)
);
    DROP TABLE public.booking;
       public         heap    postgres    false            �            1259    16467    guest    TABLE     �   CREATE TABLE public.guest (
    guestid integer NOT NULL,
    guestname character varying(255),
    guestcontactinfo character varying(255),
    guestpaymentmethod character varying(255)
);
    DROP TABLE public.guest;
       public         heap    postgres    false            �            1259    16474    room    TABLE     �   CREATE TABLE public.room (
    roomid integer NOT NULL,
    roomtype character varying(255),
    roomstatus boolean,
    roomprice double precision
);
    DROP TABLE public.room;
       public         heap    postgres    false            �            1259    16501    service    TABLE     �   CREATE TABLE public.service (
    serviceid integer NOT NULL,
    servicename character varying(255),
    staffrole character varying(255),
    staffcontactinfo character varying(255)
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    24644    servicebooking    TABLE     �   CREATE TABLE public.servicebooking (
    servicebookingid integer NOT NULL,
    roomid integer,
    serviceid integer,
    datetime date,
    paymentstatus character varying(50)
);
 "   DROP TABLE public.servicebooking;
       public         heap    postgres    false            �            1259    16494    staff    TABLE     �   CREATE TABLE public.staff (
    staffid integer NOT NULL,
    staffname character varying(255),
    staffrole character varying(255),
    staffcontactinfo character varying(255)
);
    DROP TABLE public.staff;
       public         heap    postgres    false                      0    16479    booking 
   TABLE DATA           g   COPY public.booking (bookingid, guestid, roomid, checkindate, checkoutdate, paymentstatus) FROM stdin;
    public          postgres    false    217   �                 0    16467    guest 
   TABLE DATA           Y   COPY public.guest (guestid, guestname, guestcontactinfo, guestpaymentmethod) FROM stdin;
    public          postgres    false    215   �                 0    16474    room 
   TABLE DATA           G   COPY public.room (roomid, roomtype, roomstatus, roomprice) FROM stdin;
    public          postgres    false    216   �                 0    16501    service 
   TABLE DATA           V   COPY public.service (serviceid, servicename, staffrole, staffcontactinfo) FROM stdin;
    public          postgres    false    219   /                  0    24644    servicebooking 
   TABLE DATA           f   COPY public.servicebooking (servicebookingid, roomid, serviceid, datetime, paymentstatus) FROM stdin;
    public          postgres    false    220   �                  0    16494    staff 
   TABLE DATA           P   COPY public.staff (staffid, staffname, staffrole, staffcontactinfo) FROM stdin;
    public          postgres    false    218   "!       h           2606    16483    booking booking_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_pkey PRIMARY KEY (bookingid);
 >   ALTER TABLE ONLY public.booking DROP CONSTRAINT booking_pkey;
       public            postgres    false    217            d           2606    16473    guest guest_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.guest
    ADD CONSTRAINT guest_pkey PRIMARY KEY (guestid);
 :   ALTER TABLE ONLY public.guest DROP CONSTRAINT guest_pkey;
       public            postgres    false    215            f           2606    16478    room room_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (roomid);
 8   ALTER TABLE ONLY public.room DROP CONSTRAINT room_pkey;
       public            postgres    false    216            l           2606    16507    service service_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (serviceid);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    219            n           2606    24648 "   servicebooking servicebooking_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.servicebooking
    ADD CONSTRAINT servicebooking_pkey PRIMARY KEY (servicebookingid);
 L   ALTER TABLE ONLY public.servicebooking DROP CONSTRAINT servicebooking_pkey;
       public            postgres    false    220            j           2606    16500    staff staff_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (staffid);
 :   ALTER TABLE ONLY public.staff DROP CONSTRAINT staff_pkey;
       public            postgres    false    218            o           2606    16484    booking booking_guestid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_guestid_fkey FOREIGN KEY (guestid) REFERENCES public.guest(guestid);
 F   ALTER TABLE ONLY public.booking DROP CONSTRAINT booking_guestid_fkey;
       public          postgres    false    217    215    4708            p           2606    16489    booking booking_roomid_fkey    FK CONSTRAINT     |   ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_roomid_fkey FOREIGN KEY (roomid) REFERENCES public.room(roomid);
 E   ALTER TABLE ONLY public.booking DROP CONSTRAINT booking_roomid_fkey;
       public          postgres    false    216    217    4710            q           2606    24649 )   servicebooking servicebooking_roomid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.servicebooking
    ADD CONSTRAINT servicebooking_roomid_fkey FOREIGN KEY (roomid) REFERENCES public.room(roomid);
 S   ALTER TABLE ONLY public.servicebooking DROP CONSTRAINT servicebooking_roomid_fkey;
       public          postgres    false    220    216    4710            r           2606    24654 ,   servicebooking servicebooking_serviceid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.servicebooking
    ADD CONSTRAINT servicebooking_serviceid_fkey FOREIGN KEY (serviceid) REFERENCES public.service(serviceid);
 V   ALTER TABLE ONLY public.servicebooking DROP CONSTRAINT servicebooking_serviceid_fkey;
       public          postgres    false    219    220    4716               �   x�M�11k�| �����'@�DC�NΧ �ɣ]����f�,=�����z&TQjlr���.�����\�o=n��2E�Za2è>cB<!���	��Xb[2x����^>3�4�MG}|!m�}sgk<N�0j�C/�'ܯ)�9�8�         "  x�mP�N�0<o�"�*�?r#TH�������"Vݸ�����MRNؒ�����,
��=x�I00-�1��l��W�"���vH�6]�q8��\{���ÒNλ寸?��8��]aÛ�ߣu�]ʡ}�.��46�S���N��|�I�!�^o@A8g���}�^�M�1��z&��RX%���9\h:Q��M�3����H�b���0L�Z�4Z�Lh�V(�5vZ�^��ؘ���=_��2r�@���8#+���W%E=��A�ⓒ�`���/�Ǯi�D:x�         J   x�340�,��K�I�,�440�240�L�/M�IU�)�(-��L�42��7������0+��V��qqq ��         �   x�M�=�0�g��X�$``	���Z���Tq:��Db������Zu,܄I1�l�`8H�_68G����
�m��J��Ф\�D����_qn~%���L�7�(�!��B�$3J|�%gi��Ǥi���s?v�2�         K   x�3261�440�44�4202�50"΀��.s$9]c ���� �8M���r���L!r1z\\\ �         �   x�u�OKAG��O�O0t���آ-�zA��qg3�dV�Oﴋ�����#��20v���s���+��G��|�v����ħľTm�ʙ�d��y�.�K��I�R
��7lv�9�*V ��� e�^�=��'|d����}�Ҭ-F�aU�M�Xa'c|`N����o'ǥEy�#|&�jV�|���?ŋk����s�     