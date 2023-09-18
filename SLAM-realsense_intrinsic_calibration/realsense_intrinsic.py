import pyrealsense2 as rs

if __name__ == '__main__':
    # Starts captures
    width, height, fps = 640, 480, 30

    # Sets up realsense
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, width, height, rs.format.z16, fps)
    config.enable_stream(rs.stream.color, width, height, rs.format.bgr8, fps)
    profile = pipeline.start(config)

    # Get intrinsics
    depth_sensor = profile.get_device().first_depth_sensor()
    cam_scale = depth_sensor.get_depth_scale()
    intrinsic_c =  profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()
    intrinsic_d =  profile.get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()

    # Prints intrinsics
    print(f'Color:\n{intrinsic_c}\n')
    print(f'Depth:\n{intrinsic_d}, scale: {cam_scale}\n')

    # Color:
    # [ 640x480  p[313.423 245.644]  f[379.725 379.326]  Inverse Brown Conrady [-0.0581344 0.0675349 3.28108e-05 0.000804368 -0.0214354] ]

    # Depth:
    # [ 640x480  p[320.898 233.42]  f[385.988 385.988]  Brown Conrady [0 0 0 0 0] ], scale: 0.0010000000474974513