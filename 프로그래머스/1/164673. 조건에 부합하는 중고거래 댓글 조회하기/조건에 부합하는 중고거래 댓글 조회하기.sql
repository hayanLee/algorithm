-- USED_GOODS_BOARD : 중고거래 정보
-- USED_GOODS_REPLY : 첨부파일
# 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.created_date, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD as b
join USED_GOODS_REPLY as r on b.BOARD_ID = r.BOARD_ID
where b.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-30'
order by r.created_date, b.title