import ast

def CodiPilot(values, labels=None, chart_type: str = 'bar') -> str:
    if isinstance(values, str):
        values = ast.literal_eval(values)
    if isinstance(labels, str):
        labels = ast.literal_eval(labels)
    if not values:
        return "No data provided."

    if labels is None:
        labels = [str(i) for i in range(len(values))]

    width = 600
    height = 400
    margin = 60
    chart_width = width - 2 * margin
    chart_height = height - 2 * margin

    max_val = max(values) if values else 1.0
    # Avoid division by zero when all values are the same (e.g., all zeros)
    if max_val == 0:
        max_val = 1.0
    n = len(values)

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="' + str(width) + '" height="' + str(height) + '">',
        '  <rect width="100%" height="100%" fill="white"/>',
        '  <line x1="' + str(margin) + '" y1="' + str(margin) + '" x2="' + str(margin) + '" y2="' + str(height - margin) + '" stroke="black" stroke-width="2"/>',
        '  <line x1="' + str(margin) + '" y1="' + str(height - margin) + '" x2="' + str(width - margin) + '" y2="' + str(height - margin) + '" stroke="black" stroke-width="2"/>',
    ]

    if chart_type == 'line':
        step = chart_width / (n - 1) if n > 1 else chart_width
        points = []
        for i, val in enumerate(values):
            x = margin + i * step
            y = height - margin - (val / max_val) * chart_height
            points.append(f'{x:.1f},{y:.1f}')
            svg.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="steelblue"/>')
            svg.append(f'  <text x="{x:.1f}" y="{height - margin + 15}" text-anchor="middle" font-size="12">{labels[i]}</text>')
            svg.append(f'  <text x="{x:.1f}" y="{y - 10}" text-anchor="middle" font-size="12">{val}</text>')
        svg.insert(4, f'  <polyline points="{" ".join(points)}" fill="none" stroke="steelblue" stroke-width="2"/>')
    else:
        bar_width = chart_width / n * 0.8
        gap = chart_width / n * 0.2
        for i, (val, label) in enumerate(zip(values, labels)):
            x = margin + i * (bar_width + gap) + gap / 2
            bar_height = (val / max_val) * chart_height
            y = height - margin - bar_height
            svg.append(f'  <rect x="{x:.1f}" y="{y:.1f}" width="{bar_width:.1f}" height="{bar_height:.1f}" fill="steelblue" stroke="black" stroke-width="1"/>')
            svg.append(f'  <text x="{x + bar_width / 2:.1f}" y="{height - margin + 15}" text-anchor="middle" font-size="12">{label}</text>')
            svg.append(f'  <text x="{x + bar_width / 2:.1f}" y="{y - 5}" text-anchor="middle" font-size="12">{val}</text>')

    svg.append('</svg>')

    with open('chart.svg', 'w') as f:
        f.write('\n'.join(svg))

    return 'chart.svg'
