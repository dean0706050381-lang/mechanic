# projectile_demo.py
import numpy as np
import matplotlib.pyplot as plt

# 1. 首先必须有这个函数定义
def projectile_motion(v0, theta, g=9.81, t_max=10, dt=0.01):
    """模拟抛体运动"""
    theta_rad = np.radians(theta)
    t_flight = 2 * v0 * np.sin(theta_rad) / g
    t = np.arange(0, min(t_flight, t_max), dt)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    return t, x, y

# 2. 然后才是你提供的“使用示例”部分
v0 = 20  # 初速度 20 m/s
theta = 45  # 45度角

t, x, y = projectile_motion(v0, theta)

# 3. 绘制轨迹
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=f'v0={v0}m/s, θ={theta}°')
plt.xlabel('水平距离 (m)')
plt.ylabel('垂直高度 (m)')
plt.title('抛体运动轨迹')
plt.grid(True, alpha=0.3)
plt.legend()
plt.axis('equal')
plt.show()
