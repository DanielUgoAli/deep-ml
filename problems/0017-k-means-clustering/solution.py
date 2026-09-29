import math


def distance(point1, point2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))


def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = list(initial_centroids)
    
    for _ in range(max_iterations):
        clusters = {i: [] for i in range(k)}

        for point in points:
            distances = [distance(point, centroid) for centroid in centroids]
            closest_centroid_idx = distances.index(min(distances))
            clusters[closest_centroid_idx].append(point)

        old_centroids = list(centroids)
                
        for idx in range(k):
            cluster_points = clusters[idx]
            if cluster_points:
                num_features = len(cluster_points[0])
                new_centroid = []
                for f in range(num_features):
                    feature_sum = sum(point[f] for point in cluster_points)
                    new_centroid.append(feature_sum / len(cluster_points))
                centroids[idx] = tuple(new_centroid)
                        
        if old_centroids == centroids:
            break
                    
    return centroids
