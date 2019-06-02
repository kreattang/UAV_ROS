;; Auto-generated. Do not edit!


(when (boundp 'rvo::Information)
  (if (not (find-package "RVO"))
    (make-package "RVO"))
  (shadow 'Information (find-package "RVO")))
(unless (find-package "RVO::INFORMATION")
  (make-package "RVO::INFORMATION"))

(in-package "ROS")
;;//! \htmlinclude Information.msg.html


(defclass rvo::Information
  :super ros::object
  :slots (_agent_name _agent_pose_x _agent_pose_y _agent_heading _agent_vel_mag ))

(defmethod rvo::Information
  (:init
   (&key
    ((:agent_name __agent_name) "")
    ((:agent_pose_x __agent_pose_x) 0.0)
    ((:agent_pose_y __agent_pose_y) 0.0)
    ((:agent_heading __agent_heading) 0.0)
    ((:agent_vel_mag __agent_vel_mag) 0.0)
    )
   (send-super :init)
   (setq _agent_name (string __agent_name))
   (setq _agent_pose_x (float __agent_pose_x))
   (setq _agent_pose_y (float __agent_pose_y))
   (setq _agent_heading (float __agent_heading))
   (setq _agent_vel_mag (float __agent_vel_mag))
   self)
  (:agent_name
   (&optional __agent_name)
   (if __agent_name (setq _agent_name __agent_name)) _agent_name)
  (:agent_pose_x
   (&optional __agent_pose_x)
   (if __agent_pose_x (setq _agent_pose_x __agent_pose_x)) _agent_pose_x)
  (:agent_pose_y
   (&optional __agent_pose_y)
   (if __agent_pose_y (setq _agent_pose_y __agent_pose_y)) _agent_pose_y)
  (:agent_heading
   (&optional __agent_heading)
   (if __agent_heading (setq _agent_heading __agent_heading)) _agent_heading)
  (:agent_vel_mag
   (&optional __agent_vel_mag)
   (if __agent_vel_mag (setq _agent_vel_mag __agent_vel_mag)) _agent_vel_mag)
  (:serialization-length
   ()
   (+
    ;; string _agent_name
    4 (length _agent_name)
    ;; float64 _agent_pose_x
    8
    ;; float64 _agent_pose_y
    8
    ;; float64 _agent_heading
    8
    ;; float64 _agent_vel_mag
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _agent_name
       (write-long (length _agent_name) s) (princ _agent_name s)
     ;; float64 _agent_pose_x
       (sys::poke _agent_pose_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _agent_pose_y
       (sys::poke _agent_pose_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _agent_heading
       (sys::poke _agent_heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _agent_vel_mag
       (sys::poke _agent_vel_mag (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _agent_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _agent_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _agent_pose_x
     (setq _agent_pose_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _agent_pose_y
     (setq _agent_pose_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _agent_heading
     (setq _agent_heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _agent_vel_mag
     (setq _agent_vel_mag (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get rvo::Information :md5sum-) "a69941d7ce3cf8fc435842c1ef18e37d")
(setf (get rvo::Information :datatype-) "rvo/Information")
(setf (get rvo::Information :definition-)
      "string agent_name

float64 agent_pose_x
float64 agent_pose_y
float64 agent_heading
float64 agent_vel_mag

")



(provide :rvo/Information "a69941d7ce3cf8fc435842c1ef18e37d")


