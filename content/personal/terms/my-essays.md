---
title: "My Essays"
aliases:
  - "My Essays"
  - "my essays"
date-created: 2025-01-01
---

(let* ((nodes
          (org-roam-db-query
           [:select [*]
            :from nodes
            :where (and
                    (like properties '"%form%text catalog%")
                    (like properties '"%public%true%"))]))
         (sorted-nodes
          (sort nodes
                (lambda (a b)
                  (string-lessp (nth 8 a) (nth 8 b))))))
    (mapconcat
     (lambda (node)
       (format "- [[id:%s][%s]]" (car node) (nth 8 node)))
     sorted-nodes
     "\n"))
